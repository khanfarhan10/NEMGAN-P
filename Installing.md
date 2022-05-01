# Python 2
```python
conda create --name NemGANPEnv python=2.7  
conda activate NemGANPEnv  
pip install -r requirements.txt  
tensorflow==1.5.0
```

```
ERROR: Could not find a version that satisfies the requirement tensorflow (from -r requirements.txt (line 3)) (from versions: none)
ERROR: No matching distribution found for tensorflow (from -r requirements.txt (line 3))
```
# Python 3
```python
conda create --name NemGANPEnv python=3.7  
conda activate NemGANPEnv  
pip install -r requirements_colab_modified.txt  
python nemganp_fmnist_5_py3.py
```
