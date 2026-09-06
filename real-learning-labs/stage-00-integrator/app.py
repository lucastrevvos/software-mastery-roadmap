import csv
import logging
import os
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s level=%(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)

DATA_FILE = Path(__file__).parent / "data" / "customers.csv"
SYNTHETIC_SIZE = 6000


def load_customers(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        customers = list(reader)

    logger.info(
        "event=customers_loaded env=%s count=%s path=%s",
        os.getenv("APP_ENV", "unknown"),
        len(customers),
        path,
    )
    return customers


def has_duplicate_ids(customers):
    seen = set()

    for customer in customers:
        customer_id = customer["id"]
        if customer_id in seen:
            return True
        seen.add(customer_id)

    return False


def build_synthetic_batch(customers, size=SYNTHETIC_SIZE):
    template = customers[0]
    return [
        {
            "id": f"synthetic-{index}",
            "name": f"{template['name']} {index}",
            "customer_type": template["customer_type"],
        }
        for index in range(size)
    ]


def build_report(customers):
    vip_count = sum(
        1 for customer in customers if customer["customer_type"] == "vip"
    )

    return {
        "total_customers": len(customers),
        "vip_customers": vip_count,
    }


def main():
    customers = load_customers(DATA_FILE)
    report = build_report(customers)

    synthetic_batch = build_synthetic_batch(customers)
    duplicate_ids = has_duplicate_ids(synthetic_batch)

    logger.info(
        "event=report_ready total=%s vip=%s synthetic=%s duplicate_ids=%s",
        report["total_customers"],
        report["vip_customers"],
        len(synthetic_batch),
        duplicate_ids,
    )

    print(
        f"customers={report['total_customers']} "
        f"vip={report['vip_customers']} "
        f"duplicates={duplicate_ids}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("event=app_failed")
        sys.exit(1)
