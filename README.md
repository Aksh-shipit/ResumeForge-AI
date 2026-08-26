# 🚀 ResumeForge AI

> An AI-powered resume builder that helps users create professional, ATS-friendly resumes with AI-generated content, resume analysis, ATS scoring, live preview, and PDF export.

---

## 📌 Overview

**ResumeForge AI** is a full-stack web application built with **Python and Flask** that simplifies the resume creation process.

The application allows users to create, edit, save, analyze, and download resumes while using AI to generate professional resume summaries and provide actionable improvement suggestions.

The project combines traditional web development with **Generative AI / LLM integration** to provide personalized resume assistance.

---

## ✨ Features

### 🤖 AI-Powered Features

- **AI Resume Summary Generation**
  - Generates a professional ATS-friendly summary based on:
    - Target role
    - Skills
    - Experience
  - Uses an LLM through the Groq API.

- **AI Resume Analysis**
  - Analyzes the resume using an LLM.
  - Provides actionable suggestions for improving:
    - Resume structure
    - Skills
    - Keywords
    - Experience descriptions
    - ATS compatibility

### 📊 ATS Score

The application calculates an ATS-readiness score based on resume completeness.

The scoring logic considers:

- Name
- Email
- Phone
- Professional summary
- Number of skills
- Education
- Experience
- Projects

The system also provides feedback for missing sections.

> **Note:** The current ATS score is a rule-based completeness score, not an ML-trained ATS prediction model.

### 📝 Resume Builder

Users can create resumes with:

- Personal information
- Education
- Skills
- Experience
- Projects
- Professional summary

### 👀 Live Resume Preview

The resume preview updates dynamically as the user enters information.

### 🎨 Resume Templates

Supports multiple resume templates:

- Classic ATS
- Modern Blue
- Dark Professional

### 💾 Resume Management

Users can:

- Save resumes
- View saved resumes
- Search saved resumes
- Edit resumes
- Delete resumes

### 📄 PDF Export

Users can download their completed resume as a PDF.

### 🔐 Authentication

The application includes:

- User registration
- User login
- Password hashing
- Logout
- User-specific resume storage

---

# 🏗️ Application Architecture

```text
                    ┌─────────────────────┐
                    │      User / UI      │
                    │  HTML + CSS + JS    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Flask App      │
                    │   Routes / APIs     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌─────────────┐  ┌─────────────┐
       │  SQLite DB │   │  AI Module  │  │ PDF Module  │
       │ SQLAlchemy │   │ Groq + LLM  │  │ PDF Export  │
       └────────────┘   └──────┬──────┘  └─────────────┘
                               │
                               ▼
                       ┌───────────────┐
                       │   Groq API    │
                       │   LLM Model   │
                       └───────────────┘
```
