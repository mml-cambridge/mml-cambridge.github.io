---
author: "James Elliot"
title: "Computational modelling"
date: "2023-01-23"
description: "Thoughts on modelling in materials science"
tags: ["research"]
---


With modern computational techniques, it is now possible to predict the properties of novel materials from first principles using advanced simulation techniques. This has the advantages of being both quicker and cheaper than a trial-and-error experimentation process, and also yields detailed structural and dynamical information that can provide a stringent test of theoretical models.

As computing power continues to increase at a relentless pace, it is tempting to consider the simulation of large and/or complex systems using brute force atomistic simulation methods alone. However, even extrapolating from current state-of-the-art methodologies, it would still take well over a century of exponential growth in computing resources to achieve parity with ‘real time’ simulations of experimental systems of macroscopic size and, in any case, the sheer amount of data produced would overwhelm any attempt at detailed scientific analysis. Therefore, it is imperative that we now seek to exploit the regions of overlap between well-established techniques for electronic structure calculations, molecular dynamics, mesoscopic simulations and continuum modelling to allow efficient multiscale simulations of increasingly complex condensed phase systems. Multiscale modelling is currently a powerful and widely-used tool in Materials Science, in which there have been significant technical and scientific advances over the last decade, enabling novel fields of application from nanotechnology to biomineralization.
 

In the MML group we utilise simulation techniques across all of the length scales above. At the electron scale, density functional theory and Hartree-Fock methods are used to calculate parameters ab initio. Expertise in using Materials Studio, CHARMM, AMBER, VMD, NAMD, LAMMPS, DL_POLY and many more force fields and simulation packages allow us to simulate molecular systems. In the mesoscale, coarse-grained molecular dynamics and dissipative particle dynamics are used to simulate even larger systems on timescales more comparable with experiments. Finally at the macroscopic scale the discrete element method and finite element method allow us to simulate processes which the naked eye can see.