# for testing purposes -- data sampleQueryPlan contains a list of 2 plans - standard plan and alternative plan
    
def getQueryPlan(sqlInput):

    print("**************************SQL INPUT HERE ***************************** ")
    print(sqlInput)
    sampleQueryPlan = ["""
        ('Limit  (cost=252890.86..252890.88 rows=10 width=44) (actual time=5038.191..5060.641 rows=10 loops=1)',)
        ('  ->  Sort  (cost=252890.86..254332.51 rows=576662 width=44) (actual time=5038.185..5060.634 rows=10 loops=1)',)
        ("        Sort Key: (sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))) DESC, orders.o_orderdate",)
        ('        Sort Method: top-N heapsort  Memory: 26kB',)
        ('        ->  Finalize GroupAggregate  (cost=164538.32..240429.40 rows=576662 width=44) (actual time=3861.894..4948.856 rows=145911 loops=1)',)
        ('              Group Key: lineitem.l_orderkey, orders.o_orderdate, orders.o_shippriority',)
        ('              ->  Gather Merge  (cost=164538.32..227214.22 rows=480552 width=44) (actual time=3861.880..4510.206 rows=145911 loops=1)',)
        ('                    Workers Planned: 2',)
        ('                    Workers Launched: 2',)
        ('                    ->  Partial GroupAggregate  (cost=163538.29..170746.57 rows=240276 width=44) (actual time=3698.256..4258.666 rows=48637 loops=3)',)
        ('                          Group Key: lineitem.l_orderkey, orders.o_orderdate, orders.o_shippriority',)
        ('                          ->  Sort  (cost=163538.29..164138.98 rows=240276 width=24) (actual time=3698.186..3774.811 rows=194856 loops=3)',)
        ('                                Sort Key: lineitem.l_orderkey, orders.o_orderdate, orders.o_shippriority',)
        ('                                Sort Method: external merge  Disk: 6784kB',)
        ('                                Worker 0:  Sort Method: external merge  Disk: 6840kB',)
        ('                                Worker 1:  Sort Method: external merge  Disk: 6688kB',)
        ('                                ->  Nested Loop  (cost=4521.94..137136.43 rows=240276 width=24) (actual time=125.542..3335.613 rows=194856 loops=3)',)
        ('                                      ->  Parallel Hash Join  (cost=4521.51..39222.30 rows=60057 width=12) (actual time=124.124..997.496 rows=48637 loops=3)',)
        ('                                            Hash Cond: (orders.o_custkey = customer.c_custkey)',)
        ('                                            ->  Parallel Seq Scan on orders  (cost=0.00..33907.50 rows=302198 width=16) (actual time=0.035..616.770 rows=243690 loops=3)',)
        ("                                                  Filter: (o_orderdate < '1995-03-21'::date)",)
        ('                                                  Rows Removed by Filter: 256310',)
        ('                                            ->  Parallel Hash  (cost=4366.25..4366.25 rows=12421 width=4) (actual time=123.728..123.729 rows=10063 loops=3)',)
        ('                                                  Buckets: 32768  Batches: 1  Memory Usage: 1504kB',)
        ('                                                  ->  Parallel Seq Scan on customer  (cost=0.00..4366.25 rows=12421 width=4) (actual time=0.944..110.783 rows=10063 loops=3)',)
        ("                                                        Filter: (c_mktsegment = 'HOUSEHOLD'::bpchar)",)
        ('                                                        Rows Removed by Filter: 39937',)
        ('                                      ->  Index Scan using lineitem_pkey on lineitem  (cost=0.43..1.48 rows=15 width=16) (actual time=0.039..0.044 rows=4 loops=145911)',)
        ('                                            Index Cond: (l_orderkey = orders.o_orderkey)',)
        ("                                            Filter: (l_shipdate > '1955-03-21'::date)",)
        ('Planning Time: 32.344 ms',)
        ('Execution Time: 5065.467 ms',)
        """,
        """
        ('Limit  (cost=30001262345.82..30001262345.84 rows=10 width=44) (actual time=14398.922..14398.929 rows=10 loops=1)',)
        ('  ->  Sort  (cost=30001262345.82..30001263787.47 rows=576662 width=44) (actual time=14398.920..14398.925 rows=10 loops=1)',)
        ("        Sort Key: (sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))) DESC, orders.o_orderdate",)
        ('        Sort Method: top-N heapsort  Memory: 26kB',)
        ('        ->  GroupAggregate  (cost=30000000004.66..30001249884.36 rows=576662 width=44) (actual time=3.924..14293.331 rows=145911 loops=1)',)
        ('              Group Key: lineitem.l_orderkey, orders.o_orderdate, orders.o_shippriority',)
        ('              ->  Incremental Sort  (cost=30000000004.66..30001234026.15 rows=576662 width=24) (actual time=3.903..13096.659 rows=584568 loops=1)',)
        ('                    Sort Key: lineitem.l_orderkey, orders.o_orderdate, orders.o_shippriority',)
        ('                    Presorted Key: lineitem.l_orderkey',)
        ('                    Full-sort Groups: 17190  Sort Method: quicksort  Average Memory: 27kB  Peak Memory: 27kB',)
        ('                    ->  Nested Loop  (cost=30000000001.55..30001213322.29 rows=576662 width=24) (actual time=0.965..12555.802 rows=584568 loops=1)',)
        ('                          ->  Nested Loop  (cost=20000000000.87..20000485267.10 rows=144137 width=12) (actual time=0.855..6396.383 rows=145911 loops=1)',)
        ('                                ->  Index Scan using orders_pkey on orders  (cost=10000000000.43..10000068808.43 rows=725276 width=16) (actual time=0.033..1448.228 rows=731071 loops=1)',)
        ("                                      Filter: (o_orderdate < '1995-03-21'::date)",)
        ('                                      Rows Removed by Filter: 768929',)
        ('                                ->  Memoize  (cost=0.44..4.46 rows=1 width=4) (actual time=0.006..0.006 rows=0 loops=731071)',)
        ('                                      Cache Key: orders.o_custkey',)
        ('                                      Cache Mode: logical',)
        ('                                      Hits: 631452  Misses: 99619  Evictions: 0  Overflows: 0  Memory Usage: 7317kB',)
        ('                                      ->  Bitmap Heap Scan on customer  (cost=0.43..4.45 rows=1 width=4) (actual time=0.022..0.022 rows=0 loops=99619)',)
        ('                                            Recheck Cond: (c_custkey = orders.o_custkey)',)
        ("                                            Filter: (c_mktsegment = 'HOUSEHOLD'::bpchar)",)
        ('                                            Rows Removed by Filter: 1',)
        ('                                            Heap Blocks: exact=99619',)
        ('                                            ->  Bitmap Index Scan on customer_pkey  (cost=0.00..0.43 rows=1 width=0) (actual time=0.007..0.007 rows=1 loops=99619)',)
        ('                                                  Index Cond: (c_custkey = orders.o_custkey)',)
        ('                          ->  Bitmap Heap Scan on lineitem  (cost=0.68..4.90 rows=15 width=16) (actual time=0.022..0.025 rows=4 loops=145911)',)
        ('                                Recheck Cond: (l_orderkey = orders.o_orderkey)',)
        ("                                Filter: (l_shipdate > '1955-03-21'::date)",)
        ('                                Heap Blocks: exact=154226',)
        ('                                ->  Bitmap Index Scan on lineitem_pkey  (cost=0.00..0.67 rows=15 width=0) (actual time=0.009..0.009 rows=4 loops=145911)',)
        ('                                      Index Cond: (l_orderkey = orders.o_orderkey)',)
        ('Planning Time: 0.947 ms',)
        ('Execution Time: 14404.259 ms',)
        """
        ]
    return sampleQueryPlan