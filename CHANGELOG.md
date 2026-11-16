# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2026-11-03

### Added
1. FT000: readded init.py under routes, added static folder with favico also added run.py

### Changed
1. FT000: registered blueprints in app/init.py
1. FT000: added content to README, will require fine tuning
1. FT001: updated part model, main.py, part service, and index.html to be able to select all parts and display them. migration needed to be run as well.

## 2026-11-04

### Added
1. FT002: migrations for name field in stash and many to many relationship for stash and parts, also added associations file

### Changed
1. FT002: moved part display to separate html file to test stash code