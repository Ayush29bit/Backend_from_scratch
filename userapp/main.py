from fastapi import FastAPI, HTTPException, status 
from pydantic import BaseModel, EmailStr, Field 
from typing import Optional 
from datetime import datetime

app = FastAPI()


