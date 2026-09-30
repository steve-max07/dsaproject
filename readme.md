# C-Powered Word Reverser (Full-Stack DSA Project)

A lightweight, hybrid full-stack web application that demonstrates the practical implementation of a **Stack Data Structure** using **C, Python (Flask), and Vanilla JavaScript**. 

The app takes an input word from a web browser interface, passes it down to a compiled native C binary running on the server, utilizes a stack structure to reverse it, and returns the result in real-time.

---

## 🏗️ Architecture & Data Flow

The project is built using a **three-tier architecture** that bridges high-level web APIs with low-level compiled systems:

```text
[ Frontend UI ] (HTML5 / CSS3 / Vanilla JS)
       │
       │ HTTP POST Request (JSON Payload)
       ▼
[ Backend API Wrapper ] (Python 3 / Flask / CORS Enforced)
       │
       │ Native System Subprocess Run (shell=False)
       ▼
[ Core DSA Logic Engine ] (Compiled C Binary File via GCC)
```

1. **Frontend Presentation Tier:** A minimal user interface capturing text input. It makes an asynchronous `fetch()` API call using standard JSON headers.
2. **Backend Application Wrapper Tier:** A Flask web service acting as a secure boundary. It handles CORS preflight validation, sanitizes incoming route calls, interacts with system processes via Python's `subprocess` API, and monitors process health.
3. **Core Engine Tier:** A highly optimized C program compiled straight into a native Linux binary executable via **GCC**.

---

## 🧠 Data Structure & Algorithm (DSA) Logic

This project demonstrates the classic application of a **Stack Data Structure** operating under the **LIFO (Last In, First Out)** mechanism. 

### Core Components
* **Array-based Storage:** A fixed contiguous sequence allocation in memory (`char stack[MAX_SIZE]`).
* **Top Pointer:** An integer variable `top` tracking the current array boundary element index (Initialized to `-1` to denote an empty stack).

### Operations
* **Push (`push(char ch)`):** Increments the `top` index pointer by `1` and inserts the specific character token into the newly tracked array slot.
* **Pop (`pop()`):** Extracts and returns the character token located at the current `top` array pointer, then decrements `top` by `1`.

### The Reversal Workflow

```text
Input Word: "DATA" 

[Step 1: PUSH (Left-to-Right Scan)]       [Step 2: POP (Top-to-Bottom Read)]
   
   |   A   | <-- top (Index 3)            |   A  | --> Returns 'A'
   |   T   | (Index 2)                       |   T   | --> Returns 'T'
   |   A   | (Index 1)                       |   A   | --> Returns 'A'
   |   D   | (Index 0)                       |   D  | --> Returns 'D'
   +-------+                                 +-------+ 
  Empty Stack                               Empty Stack
                                            Result: "ATAD"
```

---

## 📁 Repository Layout

```text
├── app.py                # Flask Web Server wrapper script
├── reverseword.c       # Source code for the core C Stack logic
├── index.html            # Web browser GUI interface file
├── requirements.txt      # Python dependencies list
└── README.md             # Systems documentation & architecture manual
```

---

## 🚀 Deployment Instructions (Render Cloud)

This multi-language setup is configured for seamless deployment to **Render** as a Python Web Service.

### 1. Web Service Dashboard Configurations
* **Runtime:** `Python`
* **Build Command:** Connects your dependencies and compiles the C engine on the server layout:
  ```bash
  pip install -r requirements.txt && gcc reverseword.c -o reverseword
  ```
* **Start Command:** Runs your application using a production-ready HTTP server:
  ```bash
  gunicorn app:app
  ```

### 2. Environment Variables
Render dynamically configures the allocation mapping layer, but you can explicitly specify the container port binding under the **Environment** tab if required:
* `PORT`: `10000`

### 3. Frontend Linkage
Open `index.html` and update the `BACKEND_URL` variable constant value to match your deployed Render live application service URL:
```javascript
const BACKEND_URL = "https://dsaproject-orsg.onrender.com";
```