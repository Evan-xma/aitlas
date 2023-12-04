The AiTLAS toolbox (Artificial Intelligence Toolbox for Earth Observation) includes state-of-the-art machine learning methods for exploratory and predictive analysis of satellite imagery as well as repository of AI-ready Earth Observation (EO) datasets. It can be easily applied for a variety of Earth Observation tasks, such as land use and cover classification, crop type prediction, localization of specific objects (semantic segmentation), etc. The main goal of AiTLAS is to facilitate better usability and adoption of novel AI methods (and models) by EO experts, while offering easy access and standardized format of EO datasets to AI experts which allows benchmarking of various existing and novel AI methods tailored for EO data.


# Installation

The best way to install `aitlas`, is if you create a virtual environment and install the  requirements with `pip`. Here are the steps:
- Clone this repo.
- Go to the folder where you cloned the repo.
- Create a virtual environment
```bash
conda create -n aitlas python=3.8
```
- Use the virtual environment
```bash
conda activate aitlas
```
- Install the requirements
```bash
pip install -r requirements.txt
```

After that
```bash
pip install .
```
in the folder where you cloned the repo.


---
# Citation
For attribution in academic contexts, please cite our work **'AiTLAS: Artificial Intelligence Toolbox for Earth Observation'** published in Remote Sensing (2023) [link](https://www.mdpi.com/2072-4292/15/9/2343) as

```
@article{aitlas2023,
AUTHOR = {Dimitrovski, Ivica and Kitanovski, Ivan and Panov, Panče and Kostovska, Ana and Simidjievski, Nikola and Kocev, Dragi},
TITLE = {AiTLAS: Artificial Intelligence Toolbox for Earth Observation},
JOURNAL = {Remote Sensing},
VOLUME = {15},
YEAR = {2023},
NUMBER = {9},
ARTICLE-NUMBER = {2343},
ISSN = {2072-4292},
DOI = {10.3390/rs15092343}
}
```





