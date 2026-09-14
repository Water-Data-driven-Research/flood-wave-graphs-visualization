# Flood Wave Graphs Visualization

Visualization utilities for the **Flood Wave Graphs** analytical framework.

This repository contains the plotting and visualization components used to
display graph-based flood-wave analyses, including event-level flood-wave graphs
and derived time-series outputs.

The analytical framework is maintained separately in:

https://github.com/Water-Data-driven-Research/flood-wave-graphs

The software accompanies the study:

> **Graph-based flood-wave tracking from multi-station water-level time series: a case study on the Tisza River, Central Europe**  
> Zsolt Vizi, Marcell Dabis, Norbert Deák, Balázs Mindszenti, Péter Kozák, István Fehérváry  
> *Computers & Geosciences*  
> [DOI to be added after publication]


## Purpose

The analytical framework represents detected water-level peaks as vertices of a
directed graph and temporally admissible downstream peak associations as edges.
This companion repository provides the tools used to visualize those graph
objects and related statistical outputs.

The visualization layer is intentionally separated from the analytical
implementation so that graph construction and analysis can be used independently
of a particular plotting workflow.


## Main features

The repository provides tools for visualizing outputs of the Flood Wave Graphs
framework, including:

- detected water-level peaks along a river;
- directed flood-wave graphs in a time–river-kilometre coordinate system;
- graph-defined flood waves and their downstream connections;
- reduced flood-wave graphs for selected river-section boundaries;
- annual or period-based propagation-time statistics;
- publication-ready static figures.

The exact visualizations available depend on the input objects produced by the
analytical framework.


## Relationship to the analytical framework

This repository does **not** perform the primary flood-wave detection and graph
construction.

Those steps are implemented in:

https://github.com/Water-Data-driven-Research/flood-wave-graphs

A typical workflow is:

1. load and preprocess multi-station water-level data;
2. detect local water-level peaks;
3. construct the directed flood-wave graph;
4. calculate graph-derived flood-wave statistics;
5. pass the resulting graph objects or tabular outputs to this repository for
   visualization.

For the mathematical definitions and methodology, see the accompanying paper
and the analytical repository.


## Requirements

The visualization software is implemented in **Python**.

The required packages and tested versions are listed in `requirements.txt`.
The repository uses packages including:

- `pandas`;
- `networkx`;
- `plotly`;
- `kaleido`;
- `pytest`.

No specialized hardware or GPU is required. The visualizations can be generated
on a standard desktop or laptop computer or in Google Colab.


## Installation

Clone the repository:

```bash
git clone https://github.com/Water-Data-driven-Research/flood-wave-graphs-visualization.git
cd flood-wave-graphs-visualization
```

Optionally, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```


## Input

The visualization routines operate on outputs produced by the
`flood-wave-graphs` analytical framework.

Depending on the selected visualization, the required input may contain:

- detected peak dates;
- station identifiers;
- river-kilometre positions;
- directed graph vertices and edges;
- source and destination stations;
- peak-to-peak propagation times;
- annual or section-level summary statistics.

The exact input object or table expected by each visualization routine should be
described in the corresponding function docstring or notebook example.

The Tisza River data used in the accompanying study are publicly available from:

https://drive.google.com/drive/folders/12pkrhybv52KpmeNYsHZRSkL9nfF3May2?usp=sharing


## Reproducing the manuscript figures

The complete workflow used to reproduce the plots in the accompanying manuscript
is available in the following Google Colab notebook:

https://colab.research.google.com/drive/1KYVsda0-WIYz3PhYXWa5-dc84IPo2CC4?usp=sharing

The notebook combines the analytical framework and the visualization tools and
contains the parameter settings and station selections used in the study.

In particular, it reproduces the principal visualization outputs, including:

- the event-level flood-wave graph shown for the beginning of 2001;
- the annual average peak-to-peak propagation-time series;
- the methodological graph visualizations illustrating peak detection and graph
  structure.

For complete reproducibility, the version of this repository used for the paper
should be archived as a tagged release.


## Repository structure

The repository contains the visualization package, notebooks, dependency
specification, tests, and project metadata.

A typical structure is:

```text
flood-wave-graphs-visualization/
├── fwg_visualization/      # visualization implementation
├── notebook/               # examples and visualization notebooks
├── tests/                  # automated tests, if applicable
├── requirements.txt        # Python dependencies
├── LICENSE
└── README.md
```


## Outputs

The visualization routines can produce figures such as:

- time–river-kilometre flood-wave graphs;
- peak and edge visualizations;
- reduced river-section flood-wave graphs;
- time series of annual propagation metrics;
- static image files suitable for publication.

Static figure export is supported through the visualization dependencies listed
in `requirements.txt`.


## Testing

If the repository includes automated tests, they can be run with:

```bash
pytest
```


## Data availability

The Tisza River water-level data used in the accompanying study are publicly
available and can be downloaded from:

https://drive.google.com/drive/folders/12pkrhybv52KpmeNYsHZRSkL9nfF3May2?usp=sharing


## License

This project is released under the **Apache License 2.0**.

See [LICENSE](LICENSE) for details.


## Citation

If you use this software in academic work, please cite the accompanying paper:

```bibtex
@article{vizi_flood_wave_graphs,
  title   = {Graph-based flood-wave tracking from multi-station water-level time series: a case study on the Tisza River, Central Europe},
  author  = {Vizi, Zsolt and Dabis, Marcell and Deák, Norbert and Mindszenti, Balázs and
             Kozák, Péter and Fehérváry, István},
  journal = {Computers & Geosciences},
  year    = {2026},
  doi     = {[DOI]}
}
```

For the exact software version used in the publication, cite the archived
release or DOI once available.


## Contact

For questions concerning the flood-wave framework and its visualization, please
contact:

**Zsolt Vizi**  
University of Szeged, Bolyai Institute  
Email: zsvizi@math.u-szeged.hu
