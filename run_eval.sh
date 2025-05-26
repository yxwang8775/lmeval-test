HUGGINGFACE_CKPT_PATH="/home/v-zhenghlin/hf_model/TinyLlama_v1.1"

CUDA_VISIBLE_DEVICES=0 lm_eval \
    --model hf \
    --model_args pretrained="${HUGGINGFACE_CKPT_PATH}",dtype="bfloat16",parallelize=True \
    --batch_size 8 \
    --trust_remote_code \
    --tasks logiqa \
    -o "${HUGGINGFACE_CKPT_PATH}/eval_zs_qa.json" \
    2>&1 | tee "${HUGGINGFACE_CKPT_PATH}/eval_zs_qa.txt"