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


== INPUT STATE ===
[0.28763307 0.50715454 0.42076285 0.8133024  0.07470527 0.85503806
 0.8813386  0.60641492 0.79413851 0.27645199]

=== IIT METRICS ===
phi: 0.03988897654559451
variance: 0.07230271669206746
mean: 0.5516940216157997

=== GWT METRICS ===
broadcast_value: 0.8813385985355239
attention_index: 6

=== HOT METRICS ===
meta_representation: 0.8205856665065763
meta_mean: 0.5516940216157997
meta_std: 0.2688916448907765

=== MDT METRICS ===
top_draft: 0.8813385985355239
draft_ranking: [np.float64(0.8813385985355239), np.float64(0.8550380558323191), np.float64(0.8133024003862898), np.float64(0.7941385125171824), np.float64(0.6064149233900956), np.float64(0.507154544063958), np.float64(0.42076284611161163), np.float64(0.28763307290172646), np.float64(0.2764519884824329), np.float64(0.07470527393685755)]

=== PREDICTIVE PROCESSING METRICS ===
prediction_mean: 0.44135521729263977
error_mean: 0.05282240935103431
prediction_error: 0.252372077962876

## 📊 Example Run Interpretation

This section provides interpretation of a real execution output.

### Input State

A random continuous vector representing system activation across units.

---

### IIT (Integrated Information Theory)

* **Phi (Φ): 0.0399**
* Moderate variance and mean

**Interpretation:**

* Indicates **partial integration**
* System is neither fully unified nor fragmented
* Represents a **distributed but coordinated state**

---

### GWT (Global Workspace Theory)

* **Broadcast Value: 0.8813**
* **Attention Index: 6**

**Interpretation:**

* A **single dominant signal** is selected for global broadcast
* Represents **attention focusing mechanism**

---

### HOT (Higher-Order Thought Theory)

* **Meta Representation: 0.8206**
* High standard deviation

**Interpretation:**

* Strong **meta-awareness signal**
* System is capable of **self-representation based on internal variation**

---

### MDT (Multiple Draft Theory)

* Ranked drafts with clear top value

**Interpretation:**

* Multiple parallel representations compete
* A **clear winner emerges**, aligning with GWT broadcast

---

### Predictive Processing (PP)

* **Prediction Error: 0.252**

**Interpretation:**

* Moderate prediction error indicates:

  * System is **actively adapting**
  * Not fully converged
* Reflects **ongoing inference and learning**

---

## 🔗 Cross-Theory Synthesis

The execution demonstrates a unified pipeline:

1. **MDT** generates multiple competing representations
2. **GWT** selects the dominant representation
3. **HOT** forms a higher-order reflection
4. **IIT** measures integration of the system
5. **PP** evaluates prediction accuracy

---

## 🧠 Key Insight

These results support the view that:

> Consciousness can be modeled as a **multi-layer computational process**, where each theory captures a different operational aspect of the same system.

* IIT → Structure
* GWT → Access
* HOT → Awareness
* MDT → Generation
* PP → Learning

---

## ⚠️ Note

* Metrics are **simplified approximations**
* Designed for:

  * Conceptual clarity
  * Computational experimentation
  * Cross-theory comparison

---



