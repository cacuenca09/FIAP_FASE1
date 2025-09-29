from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Configuração do Alembic
config = context.config

# Setup de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 👉 Importa o db do seu app.py
from app import db

# Alembic precisa saber do MetaData
target_metadata = db.metadata


def run_migrations_offline() -> None:
    """Rodando migrações em modo 'offline' (gera apenas SQL)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Rodando migrações em modo 'online' (conecta no banco)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
