#!/bin/bash

# PID Experiment.

## Stabilization
python3 ./pid_experiment.py --task quadrotor --algo pid --overrides ./config_pid_quadrotor_stabilization.yaml