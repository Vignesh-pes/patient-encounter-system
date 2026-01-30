# Patient Encounter Management System

## Overview
A production-grade backend system built with FastAPI, SQLAlchemy, and MySQL
to manage patients, doctors, and appointment scheduling with conflict detection.

## Tech Stack
- Python 3.10
- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- Pytest
- GitHub Actions

## Features
- Patient & doctor management
- Appointment scheduling with conflict detection
- Business-rule driven service layer
- Database migrations using Alembic
- 90%+ unit test coverage
- CI pipeline with GitHub Actions

## Project Structure


## Setup
```bash
poetry install
alembic upgrade head
uvicorn src.main:app --reload
