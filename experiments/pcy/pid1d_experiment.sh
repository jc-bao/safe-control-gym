#!/bin/bash

# PID Experiment.

## Stabilization
python3 ./pid1d_experiment.py --task quadrotor --algo pid1d --overrides ./config_pid_quadrotor_stabilization.yaml