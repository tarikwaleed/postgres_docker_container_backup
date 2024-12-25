import os
from datetime import datetime
import argparse

# Hardcoded path to pg_dump
PG_DUMP_PATH = "/usr/bin/pg_dump"


def backup_database(container_name, db_user, db_name, backup_dir):
    """Creates a backup of the PostgreSQL database."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_dir, f"{container_name}-backup-{timestamp}.sql")

    command = f"docker exec -i {container_name} {PG_DUMP_PATH} -U {db_user} {db_name} > {backup_file}"
    os.system(command)
    print(f"Backup created: {backup_file}")


def main():
    parser = argparse.ArgumentParser(description="Backup PostgreSQL database in a Docker container.")
    parser.add_argument("--container", required=True, help="Name of the Docker container.")
    parser.add_argument("--db_user", required=True, help="Database user.")
    parser.add_argument("--db_name", required=True, help="Database name.")
    parser.add_argument("--backup_dir", required=True, help="Directory to save the backup files.")

    args = parser.parse_args()

    backup_database(args.container, args.db_user, args.db_name, args.backup_dir)


if __name__ == "__main__":
    main()
