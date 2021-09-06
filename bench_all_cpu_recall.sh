DBNAME='SIFT1M'
# TOPK='1'
# TOPK='10'
TOPK='100'

# for RECALL in '20' '25' '30' # topK=1
# for RECALL in '40' '60' '80' # topK=10
for RECALL in '60' '80' '95' # topK=100
do
    echo '====================' $DBNAME 'Recall' $RECALL 'TopK' $TOPK 'Starts' '====================' >> cpu_recall
    echo ' ' >> cpu_recall

    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF1024,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF2048,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF4096,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF8192,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF16384,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF32768,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF65536,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF131072,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IVF262144,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall

    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF1024,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF2048,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF4096,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF8192,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF16384,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF32768,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF65536,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF131072,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IVF262144,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall

    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x8,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x9,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x10,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x11,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x12,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x13,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key IMI2x14,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall

    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x8,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x9,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x10,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x11,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x12,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x13,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall
    python bench_cpu_recall.py --dbname $DBNAME --index_key OPQ16,IMI2x14,PQ16 --recall_goal $RECALL --topK $TOPK >> cpu_recall

    echo '====================' $DBNAME 'Recall' $RECALL 'TopK' $TOPK 'Ends' '====================' >> cpu_recall
    echo ' ' >> cpu_recall
done
