# A custom solution for bringing legacy Machine Learning code into Amazon SageMaker

In this repository, we present a deployement-ready solution which uses [SageMaker Processing] (https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) for data processing workloads [AWS Step Functions](https://aws.amazon.com/step-functions) to orchestrate workflow on [Amazon SageMaker](https://aws.amazon.com/sagemaker/).

A complete description can be found in the corresponding [blog post]().


## Outline
- [Prerequisites](#Prerequisites)
- [Notebook Walktrough](#walktrough)
- [Repo structure](#structure)
- [Input Documentation](#doc)


## <a name="Prerequisites"></a> Prerequisites
- SageMaker Studio instance 
- Clone the provided GitHub repo into your SageMaker Studio


##  <a name="walkthrough"></a> Notebook Walkthrough (SUGGESTED)

You can familiarize with the resources using the tutorial `inferencecontainer/build_and_push.ipynb`.


# Repository file structure

The GitHub repo is organized into different folders that correspond to various stages in the machine learning lifecycle, facilitating easy navigation and management. 

* legacycode_mlops
  - inferencecontainer
    - build_and_push.ipynb
    - Dockerfile
    - src
      - predict.py
      - requirements.txt
  - preprocessing
    - preprocess.py
    - requirements.txt
  - postprocessing
    - postprocess.py
    - requirements.txt
  - data
    - pre_processing_input.csv
  - stepfunctions_config.json
  - stepfunctions_input_parameters.json
  - stepfunctions_permission_policy.json
 
 ##  <a name="doc"></a>  State Machines Input Documentation

Action flows defined using AWS Step Functions are called State Machine.
Each machine has parameters that can be defined at runtime (i.e. execution-specific) which are specified through an input json object. You can copy/paste them directly into the AWS Console.

__Request Syntax__

```
{
"PreProcessing":
  {
    "ProcessingJobName": "sm-inf-job-0211-1156",
    "InputUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/data/preproc/input/"
    },
    "OutputUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/data/predict/input/"
    },
    "CodeUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/scripts/"
    },
    "InstanceType": "ml.m5.xlarge",
    "VolumeSizeInGB": 20,
    "MaxRuntimeInSeconds": 3600,
    "ImageUri": "<account-id>.dkr.ecr.<region>.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3",
    "RoleArn": "arn:aws:iam::<account-id>:role/service-role/<AmazonSageMaker-ExecutionRole>"
  },
"Inference":
  {
    "ProcessingJobName": "sm-inf-job-0211-1157",
    "InputUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/data/predict/input/"
    },
    "OutputUri":
    {
      "S3Uri": "s3://<bucket>legacycode/data/predict/output/"
    },
    "InstanceType": "ml.m5.xlarge",
    "VolumeSizeInGB": 20,
    "MaxRuntimeInSeconds": 3600,
    "ImageUri": "<account-id>.dkr.ecr.<region>.amazonaws.com/legacycode:1.0",
    "RoleArn": "arn:aws:iam::<account-id.:role/service-role/<AmazonSageMaker-ExecutionRole>"
  },
"PostProcessing":
  {
    "ProcessingJobName": "sm-inf-job-0211-1158",
    "InputUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/data/predict/output/"
    },
    "OutputUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/data/postproc/output/"
    },
    "CodeUri":
    {
      "S3Uri": "s3://<bucket>/legacycode/scripts/"
    },
    "InstanceType": "ml.m5.xlarge",
    "VolumeSizeInGB": 20,
    "MaxRuntimeInSeconds": 3600,
    "ImageUri": "<account-id>.dkr.ecr.<region>.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3",
    "RoleArn": "arn:aws:iam::<account-id>:role/service-role/<AmazonSageMaker-ExecutionRole>"
  }
}

```
__Parameters__

- __input_uri- __ - The S3 URI for the input files.
- __output_uri- __ - The S3 URI for the output files.
- __code_uri- __ - The S3 URI for script files.
- __custom_image_uri- __ - The container URI for the custom container you have built.
- __scikit_image_uri- __ - The container URI for the pre-built Sci-kit learn framework.
- __role- __ - The execution role to run the job.
- __instance_type- __ - The instance type you need to use to run the container.
- __volume_size- __ - The storage volume size you require for the container.
- __max_runtime- __ - The maximum runtime for the container, with a default value of 1 hour.

## Enjoy!
