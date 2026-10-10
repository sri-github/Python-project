import json
import os
from fastapi import FastAPI, HTTPException
from models import Invoice

app = FastAPI()

# Path configuration for Day2 structure
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = "../data/invoices.json"

def load_invoices():
    """Step 3: Helper function to load invoices from JSON"""
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_invoices(invoices):
    """Step 4: Helper function to save invoices to JSON"""
    with open(DATA_FILE, "w") as f:
        json.dump(invoices, f, indent=4)

@app.get("/invoices")
def get_invoices():
    """Step 3: Read all invoices from JSON"""
    return load_invoices()

@app.post("/invoices", status_code=201)
def create_invoice(invoice: Invoice):
    """Step 4: Load -> Add -> Save -> Return"""
    invoices = load_invoices()
    
    # Check if ID already exists
    for inv in invoices:
        if inv["invoice_id"] == invoice.invoice_id:
            raise HTTPException(status_code=400, detail="Invoice ID already exists")
            
    invoices.append(invoice.model_dump())
    save_invoices(invoices)
    return {"message": "Invoice created successfully", "invoice": invoice}

@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: str):
    invoices = load_invoices()
    invoice_found = False
    updated_invoices = []
    
    for inv in invoices:
        if inv["invoice_id"] == invoice_id:
            invoice_found = True
        else:
            updated_invoices.append(inv)
            
    if not invoice_found:
        raise HTTPException(status_code=404, detail="Invoice not found")
        
    save_invoices(updated_invoices)
    return {"message": f"Invoice {invoice_id} deleted successfully"}