import numpy as np

# =========================
# IIT (Integrated Information Theory)
# =========================
class IIT:
    def compute_phi(self, state):
        phi = np.var(state) * np.mean(state)
        return {
            "phi": phi,
            "variance": np.var(state),
            "mean": np.mean(state)
        }


# =========================
# GWT (Global Workspace Theory)
# =========================
class GWT:
    def broadcast(self, state):
        broadcast_value = np.max(state)
        attention_index = np.argmax(state)
        return {
            "broadcast_value": broadcast_value,
            "attention_index": int(attention_index)
        }


# =========================
# HOT (Higher-Order Thought)
# =========================
class HOT:
    def higher_order(self, state):
        meta_mean = np.mean(state)
        meta_std = np.std(state)
        return {
            "meta_representation": meta_mean + meta_std,
            "meta_mean": meta_mean,
            "meta_std": meta_std
        }


# =========================
# MDT (Multiple Draft Theory)
# =========================
class MDT:
    def drafts(self, state):
        ranked = sorted(state, reverse=True)
        return {
            "top_draft": ranked[0],
            "draft_ranking": ranked
        }


# =========================
# Predictive Processing (PP)
# =========================
class PredictiveProcessing:
    def process(self, model, input_signal):
        prediction = model * 0.8
        error = input_signal - prediction
        loss = np.mean(np.abs(error))
        return {
            "prediction_mean": np.mean(prediction),
            "error_mean": np.mean(error),
            "prediction_error": loss
        }


# =========================
# MAIN EXECUTION
# =========================
def main():
    # Shared state
    state = np.random.rand(10)
    input_signal = np.random.rand(10)

    print("\n=== INPUT STATE ===")
    print(state)

    # Instantiate all models
    iit = IIT()
    gwt = GWT()
    hot = HOT()
    mdt = MDT()
    pp = PredictiveProcessing()

    # Run all theories independently
    iit_metrics = iit.compute_phi(state)
    gwt_metrics = gwt.broadcast(state)
    hot_metrics = hot.higher_order(state)
    mdt_metrics = mdt.drafts(state)
    pp_metrics = pp.process(state, input_signal)

    # =========================
    # OUTPUT (CLEARLY SEPARATED)
    # =========================

    print("\n=== IIT METRICS ===")
    for k, v in iit_metrics.items():
        print(f"{k}: {v}")

    print("\n=== GWT METRICS ===")
    for k, v in gwt_metrics.items():
        print(f"{k}: {v}")

    print("\n=== HOT METRICS ===")
    for k, v in hot_metrics.items():
        print(f"{k}: {v}")

    print("\n=== MDT METRICS ===")
    for k, v in mdt_metrics.items():
        print(f"{k}: {v}")

    print("\n=== PREDICTIVE PROCESSING METRICS ===")
    for k, v in pp_metrics.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
