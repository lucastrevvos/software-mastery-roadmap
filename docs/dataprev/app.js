const DATA_URL = "./data/course.json?v=1.0.2";
const STORAGE_KEY = "dataprev-ams-learning-progress-v1";

let courseData = null;
let flatLessons = [];
let currentLessonId = null;
let progress = loadProgress();
let sessionScores = {};

const el = (id) => document.getElementById(id);

document.addEventListener("DOMContentLoaded", init);

async function init() {
  try {
    const response = await fetch(DATA_URL, { cache: "no-store" });
    if (!response.ok) throw new Error("Não foi possível carregar o curso.");
    courseData = await response.json();

    flatLessons = courseData.modules
      .filter((module) => module.available)
      .flatMap((module) =>
        module.lessons.map((lesson) => ({
          ...lesson,
          moduleId: module.id,
          moduleTitle: module.title,
          moduleNumber: module.number
        }))
      );

    el("courseTitle").textContent = courseData.course.title;
    bindGlobalActions();
    renderCurriculum();

    const requested = location.hash.replace("#", "");
    const firstIncomplete = flatLessons.find((lesson) => !progress.completed.includes(lesson.id));
    const initial = flatLessons.some((lesson) => lesson.id === requested)
      ? requested
      : (firstIncomplete?.id || flatLessons[0]?.id);

    openLesson(initial);
  } catch (error) {
    el("lesson").innerHTML =
      '<h1>Falha ao carregar</h1><p>' + escapeHtml(error.message) + '</p>';
  }
}

function bindGlobalActions() {
  el("sidebarToggle").addEventListener("click", () => el("sidebar").classList.toggle("open"));
  el("prevButton").addEventListener("click", goPrevious);
  el("completeButton").addEventListener("click", completeCurrent);
  el("exportProgress").addEventListener("click", exportProgress);
  el("importProgress").addEventListener("change", importProgress);

  window.addEventListener("hashchange", () => {
    const id = location.hash.replace("#", "");
    if (id && id !== currentLessonId && flatLessons.some((lesson) => lesson.id === id)) {
      openLesson(id, false);
    }
  });
}

function loadProgress() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return saved && Array.isArray(saved.completed)
      ? {
          completed: saved.completed,
          scores: saved.scores || {},
          updatedAt: saved.updatedAt || null
        }
      : { completed: [], scores: {}, updatedAt: null };
  } catch {
    return { completed: [], scores: {}, updatedAt: null };
  }
}

function saveProgress() {
  progress.updatedAt = new Date().toISOString();
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  renderCurriculum();
  updateProgressSummary();
}

function isLocked(lessonId) {
  return false;
}

function renderCurriculum() {
  const nav = el("curriculum");
  nav.innerHTML = "";

  courseData.modules.forEach((module) => {
    const wrapper = document.createElement("section");
    wrapper.className = "module";

    if (module.id === getCurrentLesson()?.moduleId || module.id === "phase-00") {
      wrapper.classList.add("open");
    }

    const toggle = document.createElement("button");
    toggle.className = "module-toggle";
    toggle.innerHTML =
      '<span class="module-number">' + escapeHtml(module.number) + '</span>' +
      '<span class="module-copy"><strong>' + escapeHtml(module.title) + '</strong><small>' +
      escapeHtml(module.available ? module.label : module.label + " · em construção") +
      '</small></span>';
    toggle.addEventListener("click", () => wrapper.classList.toggle("open"));

    const list = document.createElement("div");
    list.className = "lesson-list";

    if (module.available) {
      module.lessons.forEach((lesson) => {
        const locked = isLocked(lesson.id);
        const completed = progress.completed.includes(lesson.id);
        const button = document.createElement("button");

        button.className =
          "lesson-link" +
          (lesson.id === currentLessonId ? " active" : "") +
          (completed ? " completed" : "") +
          (locked ? " locked" : "");

        button.disabled = locked;
        button.innerHTML =
          '<span class="lesson-icon">' + (completed ? "●" : "○") + '</span>' +
          '<span>' + escapeHtml(lesson.title) + '</span>' +
          '<span class="lesson-type">' + escapeHtml(typeLabel(lesson.type)) + '</span>';

        button.addEventListener("click", () => openLesson(lesson.id));
        list.appendChild(button);
      });
    } else {
      const info = document.createElement("div");
      info.className = "lesson-link locked";
      info.innerHTML =
        '<span class="lesson-icon">○</span><span>' +
        escapeHtml(module.description) +
        '</span><span class="lesson-type">PLANEJADO</span>';
      list.appendChild(info);
    }

    wrapper.append(toggle, list);
    nav.appendChild(wrapper);
  });

  updateProgressSummary();
}

function updateProgressSummary() {
  const total = flatLessons.length;
  const done = flatLessons.filter((lesson) => progress.completed.includes(lesson.id)).length;
  const percent = total ? Math.round((done / total) * 100) : 0;

  el("progressPercent").textContent = percent + "%";
  el("progressText").textContent = done + " de " + total + " etapas";
  el("progressBar").style.width = percent + "%";
}

function openLesson(id, updateHash = true) {
  const lesson = flatLessons.find((item) => item.id === id);
  if (!lesson || isLocked(id)) return;

  currentLessonId = id;

  if (updateHash) {
    history.replaceState(null, "", "#" + id);
  }

  renderCurriculum();

  el("lessonStatus").textContent =
    "Fase " + lesson.moduleNumber + " · " + typeLabel(lesson.type) +
    (progress.completed.includes(id) ? " · concluído" : "");

  el("lesson").innerHTML = renderLesson(lesson);
  wireLessonInteractions(lesson);
  updateNavigationButtons(lesson);

  window.scrollTo({ top: 0, behavior: "smooth" });
  el("sidebar").classList.remove("open");
}

function renderLesson(lesson) {
  let body =
    '<p class="eyebrow">' + escapeHtml(typeLabel(lesson.type)) + '</p>' +
    '<h1>' + escapeHtml(lesson.title) + '</h1>' +
    (lesson.lead ? '<p class="lead">' + inlineCode(lesson.lead) + '</p>' : "");

  if (lesson.blocks) body += lesson.blocks.map(renderBlock).join("");
  if (lesson.steps) body += '<h2>Roteiro</h2>' + lesson.steps.map(renderStep).join("");
  if (lesson.scenario) {
    body += '<div class="callout"><strong>Cenário</strong><br>' + inlineCode(lesson.scenario) + '</div>';
  }
  if (lesson.download) {
    body +=
      '<section class="step-card"><strong>Starter files</strong><p>' +
      inlineCode(lesson.download.note || "Baixe os arquivos desta atividade e trabalhe no seu ambiente local.") +
      '</p><p><a class="nav-button primary" href="' +
      escapeHtml(lesson.download.href) +
      '" download="' +
      escapeHtml(lesson.download.filename || "") +
      '">' +
      escapeHtml(lesson.download.label || "Baixar arquivos") +
      '</a></p></section>';
  }
  if (lesson.tasks) {
    body += '<h2>Tarefas</h2><ol>' +
      lesson.tasks.map((item) => '<li>' + inlineCode(item) + '</li>').join("") +
      '</ol>';
  }
  if (lesson.questions) body += renderQuestions(lesson);
  if (lesson.criteria) {
    body += '<h2>Critérios de conclusão</h2><ul class="checklist">' +
      lesson.criteria.map((item) => '<li>' + inlineCode(item) + '</li>').join("") +
      '</ul>';
  }

  if (lesson.type === "project") {
    body +=
      '<div class="callout"><strong>Ownership:</strong> marcar como concluído significa que você consegue explicar e defender o que produziu, não apenas que executou os comandos.</div>';
  }

  return body;
}

function renderBlock(block) {
  if (block.type === "heading") return '<h2>' + escapeHtml(block.text) + '</h2>';
  if (block.type === "paragraph") return '<p>' + inlineCode(block.text) + '</p>';
  if (block.type === "callout") return '<div class="callout">' + inlineCode(block.text) + '</div>';
  if (block.type === "bullets") {
    return '<ul>' + block.items.map((item) => '<li>' + inlineCode(item) + '</li>').join("") + '</ul>';
  }
  if (block.type === "code") {
    return '<pre><code>' + escapeHtml(block.code) + '</code></pre>';
  }
  return "";
}

function renderStep(step) {
  return (
    '<section class="step-card"><strong>' + escapeHtml(step.title) + '</strong><p>' +
    inlineCode(step.text || "") + '</p>' +
    (step.code ? '<pre><code>' + escapeHtml(step.code) + '</code></pre>' : "") +
    '</section>'
  );
}

function renderQuestions(lesson) {
  const questions = lesson.questions
    .map((question, index) => {
      const options = question.options
        .map(
          (option, optionIndex) =>
            '<label class="option"><input type="radio" name="' +
            escapeHtml(question.id) +
            '" value="' +
            optionIndex +
            '"><span>' +
            inlineCode(option) +
            '</span></label>'
        )
        .join("");

      return (
        '<section class="question-card" data-question="' +
        escapeHtml(question.id) +
        '"><strong>' +
        (index + 1) +
        ". " +
        escapeHtml(question.question) +
        '</strong><div class="options">' +
        options +
        '</div><div class="feedback" data-feedback></div></section>'
      );
    })
    .join("");

  return (
    '<div class="questions">' +
    questions +
    '</div><button class="check-answer" id="gradeQuestions">Corrigir ' +
    (lesson.type === "quiz" ? "quiz" : "checkpoint") +
    '</button><div id="scoreResult"></div>'
  );
}

function wireLessonInteractions(lesson) {
  if (!lesson.questions) return;
  const grade = document.getElementById("gradeQuestions");
  grade.addEventListener("click", () => gradeLesson(lesson));
}

function gradeLesson(lesson) {
  let correct = 0;
  let answered = 0;

  lesson.questions.forEach((question) => {
    const card = document.querySelector(
      '[data-question="' + CSS.escape(question.id) + '"]'
    );
    const selected = card.querySelector("input:checked");
    const feedback = card.querySelector("[data-feedback]");

    feedback.className = "feedback show";

    if (!selected) {
      feedback.classList.add("bad");
      feedback.textContent = "Selecione uma resposta antes de concluir.";
      return;
    }

    answered += 1;
    const selectedIndex = Number(selected.value);

    if (selectedIndex === question.answer) {
      correct += 1;
      feedback.classList.add("ok");
      feedback.textContent = question.explanation;
    } else {
      feedback.classList.add("bad");
      feedback.textContent = "Ainda não. " + question.explanation;
    }
  });

  const percent = Math.round((correct / lesson.questions.length) * 100);
  const passed =
    answered === lesson.questions.length &&
    percent >= (lesson.passPercent || 100);

  sessionScores[lesson.id] = {
    correct,
    total: lesson.questions.length,
    percent,
    passed
  };

  progress.scores[lesson.id] = sessionScores[lesson.id];
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));

  el("scoreResult").innerHTML =
    '<div class="score-card"><strong>' +
    correct +
    "/" +
    lesson.questions.length +
    " · " +
    percent +
    '%</strong><br>' +
    (passed
      ? "Gate atingido. Você pode continuar."
      : "Gate ainda não atingido. Revise os erros e tente novamente.") +
    '</div>';

  updateNavigationButtons(lesson);
}

function updateNavigationButtons(lesson) {
  const index = flatLessons.findIndex((item) => item.id === lesson.id);
  el("prevButton").disabled = index <= 0;

  const alreadyDone = progress.completed.includes(lesson.id);
  const score = sessionScores[lesson.id] || progress.scores[lesson.id];
  const gated = ["checkpoint", "quiz"].includes(lesson.type);
  const canComplete = alreadyDone || !gated || Boolean(score?.passed);

  el("completeButton").disabled = !canComplete;
  el("completeButton").textContent = alreadyDone
    ? index === flatLessons.length - 1
      ? "Concluído ✓"
      : "Continuar →"
    : "Concluir e continuar →";
}

function completeCurrent() {
  const lesson = getCurrentLesson();
  if (!lesson) return;

  const score = sessionScores[lesson.id] || progress.scores[lesson.id];

  if (["checkpoint", "quiz"].includes(lesson.type) && !score?.passed) {
    return;
  }

  if (!progress.completed.includes(lesson.id)) {
    progress.completed.push(lesson.id);
    saveProgress();
  }

  const index = flatLessons.findIndex((item) => item.id === lesson.id);
  const next = flatLessons[index + 1];

  if (next) {
    openLesson(next.id);
  } else {
    showCompletion();
    openLesson(lesson.id);
  }
}

function goPrevious() {
  const index = flatLessons.findIndex((lesson) => lesson.id === currentLessonId);
  if (index > 0) openLesson(flatLessons[index - 1].id);
}

function getCurrentLesson() {
  return flatLessons.find((lesson) => lesson.id === currentLessonId);
}

function showCompletion() {
  const lesson = getCurrentLesson();
  const module = courseData.modules.find((item) => item.id === lesson?.moduleId);
  el("resultContent").innerHTML =
    '<p class="eyebrow">MASTERY GATE</p>' +
    '<h2>' + escapeHtml(module?.title || "Tema concluído") + '</h2>' +
    '<p>O ciclo AMS deste tema foi concluído: Theory → Checkpoint → Workshop → Lab → Review → Quiz → Gate.</p>';
  el("resultDialog").showModal();
}

function exportProgress() {
  const payload = {
    schemaVersion: 1,
    courseId: courseData.course.id,
    courseVersion: courseData.course.version,
    exportedAt: new Date().toISOString(),
    progress
  };

  const blob = new Blob([JSON.stringify(payload, null, 2)], {
    type: "application/json"
  });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = "dataprev-ams-progress.json";
  anchor.click();
  URL.revokeObjectURL(url);
}

async function importProgress(event) {
  const file = event.target.files?.[0];
  if (!file) return;

  try {
    const payload = JSON.parse(await file.text());

    if (payload.courseId !== courseData.course.id || !payload.progress) {
      throw new Error("Arquivo de progresso incompatível.");
    }

    progress = {
      completed: Array.isArray(payload.progress.completed)
        ? payload.progress.completed
        : [],
      scores: payload.progress.scores || {},
      updatedAt: payload.progress.updatedAt || null
    };

    saveProgress();

    const firstIncomplete = flatLessons.find(
      (lesson) => !progress.completed.includes(lesson.id)
    );

    openLesson(firstIncomplete?.id || flatLessons[flatLessons.length - 1].id);
  } catch (error) {
    alert(error.message);
  } finally {
    event.target.value = "";
  }
}

function typeLabel(type) {
  return (
    {
      theory: "Teoria",
      checkpoint: "3 perguntas",
      workshop: "Workshop",
      lab: "Laboratório",
      review: "Review",
      quiz: "Quiz",
      project: "Gate"
    }[type] || type
  );
}

function inlineCode(text) {
  const escaped = escapeHtml(text);
  return escaped.replace(/\x60([^\x60]+)\x60/g, "<code>$1</code>");
}

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
