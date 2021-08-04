# Aggregation Pipelines
Pipeline is used to perform miltiple steps sequencly
  * Helps in writing more Expressive Queries
  * In MongoDB these Pipeline r calles Aggregation Pipelines
  * Output of ome stage is imput of next stage
  * `Only Output of final stage is written as Output`

`Input ==> `Filter` => `Transform` => `Sort` ==> Output`

* A framework based on data-processing Pipeline
* Each Piple have several stages shown above
* Output of one is input of next stage
* Last stage returns output


> *`Aggregation Pipeline defined by aggregation method`
  * inside this pass Pipelines stages as array
  * documnets passed inside stages are in sequences
  * Arrays are defined by `aggregation_stage` operators
  