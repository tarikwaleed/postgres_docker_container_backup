# PostgreSQL Database Backup Script

This project provides a Python script for automating the backup of a PostgreSQL database running inside a Docker
container. The script uses the `pg_dump` utility to create backups and saves them with a timestamped filename in a
specified directory. The script is designed to work with a cron job for periodic execution.


---

## Requirements

- Python 3.8+
- Docker installed and running
- A PostgreSQL database running inside a Docker container
- Cron (for scheduling backups)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:tarikwaleed/postgres_docker_container_backup.git
   cd postgres_docker_container_backup
   ```

2. **Install Python**:
   Ensure Python 3.6 or later is installed on your system. You can check with:
   ```bash
   python3 --version
   ```

3. **Make the Script Executable**:
   ```bash
   chmod +x backup.py
   ```

---

## Manual Usage

Run the script manually with the following command:

```bash
python3 backup.py \
  --container <docker_container_name> \
  --db_user <database_user> \
  --db_name <database_name> \
  --backup_dir <path_to_backup_directory>
```

- **`--container`**: The name of the Docker container running PostgreSQL.
- **`--db_user`**: The PostgreSQL username.
- **`--db_name`**: The name of the database to back up.
- **`--backup_dir`**: The directory where backups will be saved.

### Example:

```bash
python3 backup.py \
  --container prod_monhna_django_app_postgres_container \
  --db_user myuser \
  --db_name mydatabase \
  --backup_dir /path/to/backup_directory
```

---

## Scheduling with Cron

To automate the backups, set up a cron job:

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script to run every hour:

```bash
0 * * * * /usr/bin/python3 /path/to/backup.py \
  --container prod_monhna_django_app_postgres_container \
  --db_user myuser \
  --db_name mydatabase \
  --backup_dir /path/to/backup_directory >> /path/to/backup.log 2>&1
```

3. Save and exit. Verify the cron job with:
   ```bash
   crontab -l
   ```

---


## Notes

- Ensure the backup directory is writable by the script.
- Make sure the `pg_dump` utility is installed inside the Docker container.
- Verify the database user has sufficient permissions for backups.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

This snippet is ready to be copied and saved as a `README.md` file. Let me know if you need further adjustments!