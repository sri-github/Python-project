# Persistent Invoice API (FastAPI & JSON)

## Overview
A persistent FastAPI-based invoice management application that stores data in a JSON file (`data/invoices.json`) to ensure records survive server restarts[cite: 2].

## Project Structure
- `main.py`: Contains FastAPI application routes (`GET`, `POST`, `PUT`, `DELETE`) and JSON file handling logic.
- `models.py`: Defines the Pydantic data models (`Invoice`).
- `data/invoices.json`: JSON file acting as the persistence storage layer.

## Endpoints
- **GET /invoices**: Retrieves all invoice records from `invoices.json`[cite: 3].
- **GET /invoices/{invoice_id}**: Retrieves a single invoice by ID or returns a `404` error[cite: 5].
- **POST /invoices**: Creates a new invoice, saves it to the JSON file, and returns a `201` status[cite: 5].
- **PUT /invoices/{invoice_id}**: Updates an existing invoice and persists the changes.
- **DELETE /invoices/{invoice_id}**: Removes an invoice by ID and updates the JSON file[cite: 5].

## How to Run
1. Navigate to the `Day2` directory:
   ```bash
   cd Day2