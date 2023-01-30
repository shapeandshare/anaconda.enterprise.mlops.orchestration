#  Anaconda Enterprise MLOps Toolbox

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_anaconda.enterprise.mlops.toolbox&metric=bugs)](https://sonarcloud.io/summary/new_code?id=shapeandshare_anaconda.enterprise.mlops.toolbox)

## Overview

The toolbox provides a set of notebooks useful for MLFlow and MLOps related tasks within Anaconda Enterprise.

## Project Structure

```
root
│
└───notebooks
│   │
│   └───infrastructure
│   │       tracking_server.ipynb
│   │       tracking_server_prune.ipynb
│   │       
│   └───endpoint
│           deploy_endpoint.ipynb
│           prediction_endpoint_taxi.ipynb       
│           prediction_endpoint_wine.ipynb       
```

## Notebooks

### Infrastructure Notebooks

* [MLFlow Tracking Server Installation](notebooks/infrastructure/tracking_server.ipynb)
* [MLFlow Tracking Server Pruning Service Installation](notebooks/infrastructure/tracking_server_prune.ipynb)

### Model Endpoint Notebooks
* [MLFlow Model Serving Endpoint Deployment](notebooks/endpoint/endpoint_deploy.ipynb)
* [MLFlow Model Serving Endpoint (Taxi Recipe) Example](notebooks/endpoint/endpoint_prediction_taxi.ipynb)
* [MLFlow Model Serving Endpoint (Wine Quality Multistep Workflow) Example](notebooks/endpoint/endpoint_prediction_wine.ipynb)

## Requirements

* conda
* keyring
* anaconda-project

## Environment Setup

> anaconda-project prepare

## Anaconda Project Commands

These commands are used during develop for solution management.

| Command          | Environment  | Description                                           |
|------------------|--------------|:------------------------------------------------------|
| bash             | Development  | Enters a bash shell within the `default` environment. |
| clean            | Development  | Cleanup temporary project files                       |
| lint             | Development  | Perform code linting check                            |
| lint:fix         | Development  | Perform automated code formatting                     |

## Contributing

1. Fork the repository on GitHub
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using GitHub

## License and Authors

Copyright (c) 2023 Anaconda, Inc.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

