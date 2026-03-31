# Arch chart example

Example of using llama stack and llm-service architecture charts to host a model.

Uses [llama-stack](https://github.com/rh-ai-quickstart/ai-architecture-charts/tree/main/llama-stack) and [llm-service](https://github.com/rh-ai-quickstart/ai-architecture-charts/tree/main/llm-service) Helm charts to deploy `meta-llama/Llama-3.2-3B-Instruct` backed by vLLM on NVIDIA GPU nodes.

---

## Prerequisites

- OpenShift cluster with NVIDIA GPU nodes (nodes must have the `g5-gpu=true:NoSchedule` taint)
- Helm 3.x
- `oc` configured against your cluster
- A [Hugging Face](https://huggingface.co) account with access to the Llama 3.2 model, and a token exported as `HF_TOKEN`

```bash
export HF_TOKEN=<your-huggingface-token>
```

---

## 1. Download chart dependencies

```bash
helm dependency update ./helm
```

---

## 2. Deploy

```bash
helm install arch-chart-example ./helm \
  --set llm-service.secret.hf_token=$HF_TOKEN
```

---

## 3. Wait for pods to be ready

```bash
oc get pods -w
```

---

## 4. Port-forward the llama-stack endpoint

```bash
oc port-forward svc/llamastack 8321:8321
```

---

## 5. Run the test script

```bash
pip install llama-stack-client

python test_chat.py --endpoint http://localhost:8321
```

---

## Uninstall

```bash
./uninstall.sh
```

---
