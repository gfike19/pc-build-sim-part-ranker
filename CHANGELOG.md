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

## 2026-11-17
### Changed
1. FT002: updated stash to have unique name, stash service to have create method, main and index to handle html page and db operations to create stash, started session work

## 2026-11-21
### Changed
1. FT003: removed references and/or commented out to session for saving items between pages, 
### Removed
1. FT003: removed create stash html file
### Added
1. FT003: added action to create stash instead of just form submit

## 2026-11-22
### Changed
1. FT003: updated stash service to have get by id method, delte by id uses it, fixed issue in html where delete wasn't working, removed excess code from main and verified exception raised by service works when invalid id present
### Removed
1. FT003: removed separate create stash html

## 2026-11-23
### Changed
1. FT004: updated add part html and routes to view edit stash
### Added
1. FT004: added ability to add parts to stash, made changes to stash service and main.py

## 2026-11-25
## Added
1. FT005: can view parts in current stash on view edit stash page, can also add parts to current stash and available parts are updated