# alembic-postgis-template
Template for working with `alembic` and _**PostGIS**_ extension for _**PostgreSQL**_.

## General info
* This project uses Anaconda as environment manager. Please, make sure you have installed Anaconda or Miniconda on your machine.
* Docker-Compose is used to create a local instance of `PostGIS` database called `geo`. See [docker-compose.yml](docker-compose.yml) for more info.
* Configuration settings are located in [config.py](src/config.py) - please, do not hardcode secrets here.
* This project uses git-hooks to check code quality when creating commits. See [Git-Hooks](#git-hooks) section for more info.

## Local env setup
* Create: `conda env create -f env.yaml`
* Update: `conda env update -f env.yaml`
* Start DB container: `docker-compose up -d`
* Run migration scripts: see [Migrations](#migrations) section

## Git-Hooks
This project uses `pre-commit` package for managing and maintaining pre-commit hooks.

To ensure code quality - please make sure that you have it configured.

1. Install `pre-commit` and following packages: `isort`, `black`, `flake8`, `pytest`. You can do so by updating your
   current environment. Activate your environment and then run: `conda env update -f ./env.yaml`
2. Install pre-commit hooks by running: `pre-commit install`
3. The command above will automatically run formatters, code checks and other steps defined in the `.pre-commit-config.yaml`
4. All of those checks will also be run whenever a new commit is being created i.e. when you run `git commit -m "blah"`
5. You can also run it manually with this command: `pre-commit run --all-files`
6. **IMPORTANT!** You can manually disable pre-commit hooks by running: `pre-commit uninstall`
   Use this only in exceptional cases.

## Migrations
### DB connection
Ensure you have access to the DB. By default, locally hosted PostgreSQL instance is used.
See [config.py](src/config.py) for connection details.

### Alembic
This project uses `Alembic` for migration management. Change your current working directory to:
`./src/db`. After that you'll be able to run basic commands:

(click to expand)

<details>
<summary><b>Check history</b></summary>

```shell
alembic history
```

</details>

<details>

<summary><b>Add new (empty) migration manually</b></summary>

```shell
alembic revision -m "migration message"
```

> This will generate migration script like this:

```python
"""migration message

Revision ID: 3487cab3febf
Revises:
Create Date: 2021-11-03 18:00:25.288281

"""

# revision identifiers, used by Alembic.
revision = '3487cab3febf'
down_revision = None
branch_labels = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
```

</details>

<details>
<summary><b>Add new autogenerated migration</b></summary>

```shell
alembic revision --autogenerate -m "migration message"
```

> Assuming that we have 1 new entity named Location, this should result in a migration script
> like this:

```python
"""Add location entity

Revision ID: bc805f79e5e5
Revises: 3487cab3febf
Create Date: 2021-11-03 18:15:13.302657

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "bc805f79e5e5"
down_revision = "3487cab3febf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "location",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("created_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "extent",
            geoalchemy2.types.Geometry(geometry_type="POLYGON", srid=4326, from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="geo",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("location", schema="geo")
    # ### end Alembic commands ###

```

</details>

<details>
<summary><b>Upgrade DB to the newest migration</b></summary>

> This will run all migrations in order, that they were created.

```shell
alembic upgrade head
```

</details>

<details>
<summary><b>Rollback last migration</b></summary>

> This will roll back last migration.

```shell
alembic downgrade -1
```

</details>

<details>
<summary><b>Rollback N last migrations</b></summary>

> This will roll back last N migrations.

```shell
alembic downgrade -N
```

</details>

<details>
<summary><b>Rollback all migrations</b></summary>

> This will roll back all migrations.

```shell
alembic downgrade base
```

</details>

### Notes

Always make sure the _autogenerated_ migration scripts are valid and no unwanted stuff was added.

To learn more visit this resources:

* [sqlalchemy](https://www.sqlalchemy.org/)
* [geoalchemy-2](https://geoalchemy-2.readthedocs.io/en/latest/index.html)
* [alembic-tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)