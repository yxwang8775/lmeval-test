HUGGINGFACE_CKPT_PATH=/mnt/we/checkpoints/OpenPAI-Pretrain-20BA07B-wobias-A100-rand-1-6-batch-0613/hf_iter_67000


export HF_ENDPOINT='https://huggingface.co'
CUDA_VISIBLE_DEVICES=0 lm_eval \
    --model hf \
    --model_args pretrained="${HUGGINGFACE_CKPT_PATH}",dtype="bfloat16",parallelize=True \
    --batch_size 1 \
    --trust_remote_code \
    --tasks "arc_challenge,boolq,hellaswag,openbookqa,winogrande" \
    -o "${HUGGINGFACE_CKPT_PATH}/eval_zs_qa.json" \
    2>&1 | tee "${HUGGINGFACE_CKPT_PATH}/eval_zs_qa.txt"
