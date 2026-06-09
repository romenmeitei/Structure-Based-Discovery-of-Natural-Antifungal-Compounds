# Structure-Based Discovery of Natural Antifungal Compounds Targeting CYP51 and PksP Proteins of *Aspergillus* and *Penicillium* Species

## Overview

This repository contains the datasets, scripts, and supplementary files used for the identification and validation of fungal drug targets employed in the study:

**"Structure-Based Discovery of Natural Antifungal Compounds Targeting CYP51 and PksP Proteins of Aspergillus and Penicillium Species Through Comparative Protein Modeling, Molecular Docking and Molecular Dynamics Simulations"**

The repository has been made publicly available to ensure transparency, reproducibility, and compliance with FAIR (Findable, Accessible, Interoperable, and Reusable) data principles.

---

# Study Objectives

The study aimed to:

1. Identify clinically relevant fungal drug targets.
2. Retrieve and curate high-quality protein sequences.
3. Generate and validate three-dimensional protein structures.
4. Screen natural compounds against fungal targets using molecular docking.
5. Evaluate lead compounds using molecular dynamics simulations.
6. Investigate potential antifungal mechanisms targeting:

   * CYP51 (Sterol 14α-demethylase)
   * PksP/Alb1 (Polyketide synthase)

---

# Target Proteins

| Organism                | Target Protein | Biological Function      |
| ----------------------- | -------------- | ------------------------ |
| *Aspergillus fumigatus* | PksP/Alb1      | DHN-melanin biosynthesis |
| *Aspergillus niger*     | CYP51          | Ergosterol biosynthesis  |
| *Penicillium oxalicum*  | CYP51          | Ergosterol biosynthesis  |

---

# Repository Structure

```text
├── data/
│   ├── all_candidate_sequences.csv
│   ├── selected_sequence_summary.csv
│   └── validated_target_protein_sequences.zip
│
├── notebooks/
│   └── Extraction_of_Protein_Seq_for_target_protein_of_antifungal.ipynb
│
├── structures/
│   ├── AlphaFold/
│   ├── ColabFold/
│   ├── SWISSMODEL/
│   └── Modeller/
│
├── docking/
│   ├── ligand_structures/
│   ├── docking_results/
│   └── interaction_analysis/
│
├── md_simulation/
│   ├── APO/
│   ├── Voriconazole/
│   └── Farnesol/
│
└── README.md
```

---

# Protein Sequence Retrieval Workflow

Protein sequences were retrieved automatically using a custom Python workflow implemented in Google Colab.

The workflow performs:

### Step 1: Query NCBI Protein Database

Protein-specific search terms were generated for:

* PksP
* Alb1
* CYP51
* ERG11
* Sterol 14α-demethylase

using the NCBI Entrez API.

### Step 2: Candidate Sequence Retrieval

For each target:

* Up to 30 candidate proteins were retrieved.
* FASTA records were downloaded.
* Protein annotations were extracted.

### Step 3: Automated Filtering

Sequences were filtered using:

#### Annotation Filters

Examples:

```text
PksP
Alb1
Polyketide synthase
Conidial pigment

CYP51
ERG11
Lanosterol demethylase
Sterol 14-alpha demethylase
```

#### Length Filters

| Protein | Expected Length |
| ------- | --------------- |
| CYP51   | 450–600 aa      |
| PksP    | 1500–3000 aa    |

### Step 4: Candidate Ranking

Sequences satisfying both:

* Annotation criteria
* Length criteria

were shortlisted.

### Step 5: Manual Verification

Final target proteins were manually inspected to confirm:

* Functional annotation
* Organism identity
* Sequence completeness

before downstream structural modeling.

---

# Included Datasets

## all_candidate_sequences.csv

Contains:

* All candidate proteins retrieved from NCBI.
* Annotation information.
* Sequence lengths.
* Filtering results.

Useful for reproducing target selection decisions.

---

## selected_sequence_summary.csv

Contains:

* Final selected targets.
* Protein descriptions.
* Sequence lengths.
* Accession identifiers.

These proteins were used for structural modeling.

---

## validated_target_protein_sequences.zip

Contains:

* Final curated FASTA files.
* Protein sequences used for:

  * AlphaFold
  * ColabFold
  * SWISS-MODEL
  * Modeller

---

# Google Colab Workflow

Notebook:

```text
Extraction_of_Protein_Seq_for_target_protein_of_antifungal.ipynb
```

Purpose:

* Automated target retrieval
* Sequence filtering
* Candidate ranking
* FASTA export
* Summary table generation

This notebook allows complete reproduction of the target-identification process.

---

# Computational Pipeline

```text
Protein Retrieval
        ↓
Sequence Validation
        ↓
Structure Modeling
        ↓
Model Validation
        ↓
Ligand Preparation
        ↓
Molecular Docking
        ↓
Interaction Analysis
        ↓
Molecular Dynamics Simulation
        ↓
Trajectory Analysis
```

---

# Software and Resources

| Software                    | Version        |
| --------------------------- | -------------- |
| Python                      | 3.x            |
| Biopython                   | Latest         |
| Google Colab                | Cloud Platform |
| AlphaFold                   | v2             |
| ColabFold                   | Latest         |
| SWISS-MODEL                 | Web Server     |
| Modeller                    | v10.x          |
| PyRx                        | 0.8            |
| AutoDock Vina               | 1.2            |
| PyMOL                       | 2.x            |
| Discovery Studio Visualizer | 2021           |
| GROMACS                     | 2024.3         |

---

# Reproducibility Statement

All protein sequences, candidate retrieval records, and sequence-selection workflows used in this study have been deposited in this repository to ensure complete reproducibility of the target-identification process.

The provided datasets and Google Colab notebook allow independent researchers to reproduce sequence retrieval, filtering, and target selection from publicly available NCBI resources.

---

# Citation

If you use this dataset or workflow, please cite:

Romen Meitei et al.

"Structure-Based Discovery of Natural Antifungal Compounds Targeting CYP51 and PksP Proteins of Aspergillus and Penicillium Species Through Comparative Protein Modeling, Molecular Docking and Molecular Dynamics Simulations."

(Manuscript under preparation)

---

# License

This repository is released under the MIT License.

Researchers are free to use, modify, and distribute the data and scripts with appropriate citation.
