#  Anaconda Enterprise MLOps Orchestration Toolbox

Overview
--------
The toolbox exists to solve several goals:

1. Provides a standard platform for deploying an MLFlow Tracking Server into Anaconda Enterprise hosted environment.
2. Provide guidance and examples for leveraging MLFlow and Anaconda Enterprise.

This solution is an Anaconda Project, and as such the configuration is controlled with `anaconda-project.yml`.
The configuration file has been pre-populated with the defaults but a `prepare` can be used to create the configuration and runtime environment suiteable for deployment.

Notebooks
--------
* `notebooks` contains the notebook installations and examples.

Requirements
--------
* conda
* anaconda-project

Environment Setup
--------
> anaconda-project prepare

Anaconda Project Commands
--------
These commands are used during develop for solution management.

| Command          | Environment  | Description                                               |
|------------------|--------------|:----------------------------------------------------------|
| bash             | Development  | Enters a bash shell within the `development` environment. |
| clean            | Development  | Cleanup temporary project files                           |
| lint             | Development  | Perform code linting check                                |
| lint:fix         | Development  | Perform automated code formatting                         |

Contributing
------------
1. Fork the repository on GitHub
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using GitHub

License and Authors
-------------------
Copyright (c) 2023 Joshua Burt
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

Neither the name of Continuum Analytics, Inc. (dba Anaconda, Inc.)
("Continuum") nor the names of any contributors may be used to endorse or
promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
