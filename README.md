# ConsciousnessBrain

# 🧠 Unified Consciousness Theories Framework

## Overview

This project implements a **unified computational framework of major theories of consciousness** within a single executable `main.py`.

The system integrates:

* **Integrated Information Theory (IIT)**
* **Global Workspace Theory (GWT)**
* **Higher-Order Thought Theory (HOT)**
* **Multiple Draft Theory (MDT)**
* **Predictive Processing (PP)**

Each theory is modeled as an **independent module**, but all operate on a **shared input state**, enabling **direct comparison of outputs and metrics**.

---

## 🧩 Architecture

```
Shared Input State
        ↓
+-----------------------------+
|   IIT   |   GWT   |   HOT   |
|  (Φ)    | Broadcast | Meta  |
+-----------------------------+
|   MDT   |   PP             |
| Drafts  | Prediction Error |
+-----------------------------+
        ↓
   Structured Outputs
```

* **Single file (`main.py`)**
* Modular class-based design
* Independent execution per theory
* Unified output pipeline

---

## ⚙️ Theories Implemented

### 1. Integrated Information Theory (IIT)

* Measures **information integration**
* Metric:

  * `phi` (Φ approximation)
  * Variance
  * Mean

---

### 2. Global Workspace Theory (GWT)

* Models **attention and broadcast**
* Metric:

  * `broadcast_value`
  * `attention_index`

---

### 3. Higher-Order Thought (HOT)

* Models **meta-awareness**
* Metric:

  * `meta_representation`
  * Mean and standard deviation

---

### 4. Multiple Draft Theory (MDT)

* Models **parallel competing representations**
* Metric:

  * Ranked drafts
  * Top draft

---

### 5. Predictive Processing (PP)

* Models **brain as prediction-error minimizer**
* Metric:

  * Prediction mean
  * Error mean
  * Prediction error (loss)

---

## ▶️ How to Run

### Requirements

* Python 3.x
* NumPy

Install dependency:

```bash
pip install numpy
```

---

### Execute

```bash
python main.py
```

---

## 📤 Sample Output

```
=== INPUT STATE ===
[0.12 0.45 0.78 ...]

=== IIT METRICS ===
phi: 0.23
variance: 0.08
mean: 0.52

=== GWT METRICS ===
broadcast_value: 0.78
attention_index: 2

=== HOT METRICS ===
meta_representation: 0.61
meta_mean: 0.52
meta_std: 0.09

=== MDT METRICS ===
top_draft: 0.78
draft_ranking: [0.78, 0.65, ...]

=== PREDICTIVE PROCESSING METRICS ===
prediction_mean: 0.41
error_mean: 0.05
prediction_error: 0.12
```

---

## 🧠 Interpretation

This framework demonstrates that:

* Consciousness theories can be **modeled computationally**
* These theories are **complementary, not mutually exclusive**
* A single system can exhibit:

  * Integration (IIT)
  * Broadcasting (GWT)
  * Self-reflection (HOT)
  * Parallel cognition (MDT)
  * Prediction (PP)

---

## 🔧 Design Principles

* **Modularity** → Each theory is isolated
* **Shared State** → Enables fair comparison
* **Extensibility** → Easy to upgrade models
* **Clarity** → Clean metric separation

---

## 🚀 Future Enhancements

* Replace random inputs with:

  * Neural embeddings (LSTM / Transformer)
* Upgrade IIT:

  * Entropy / mutual information graphs
* Upgrade GWT:

  * Attention mechanisms
* Upgrade PP:

  * Variational inference (ELBO)
* Add visualization:

  * Graphs for Φ, attention, and error

---

## 📚 References

* Tononi, G. — Integrated Information Theory
* Baars, B. — Global Workspace Theory
* Rosenthal, D. — Higher-Order Thought Theory
* Dennett, D. — Multiple Draft Theory
* Friston, K. — Predictive Processing

---

## 📌 Notes

* This is a **simplified computational abstraction**, not a full biological model
* Designed for:

  * Research exploration
  * Educational use
  * AI-consciousness experimentation

---

## 👨‍💻 Author

* Unified framework design and implementation
* Assisted by generative AI (ChatGPT)

---
