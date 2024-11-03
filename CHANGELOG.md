<!--next-version-placeholder-->

## v0.3.0 (2024-11-03)

### Features

* feat: add Google Chrome and Playwright installation in Dockerfile.dev ([`2051460`](https://github.com/entelecheia/gdelt-climaterisk/commit/2051460dafc3ff6e75364e4f0e2d03505f3b09db))

* feat: add crawl4ai and nest-asyncio dependencies in pyproject.toml ([`c342a94`](https://github.com/entelecheia/gdelt-climaterisk/commit/c342a94884fd6a9cbcc86b6baac4996303d5184f))

### Refactoring

* refactor: enhance download_gdelt_gkg function with input validation and error handling ([`f0b0f09`](https://github.com/entelecheia/gdelt-climaterisk/commit/f0b0f09fe53e552100be860dff2549e7d4b1d86a))

### Unknown

* Merge pull request #11 from entelecheia/main ([`ef0756a`](https://github.com/entelecheia/gdelt-climaterisk/commit/ef0756ae8da4407c399fff55171539d289a728be))

* Merge pull request #9 from entelecheia/release

Release ([`9f0e53a`](https://github.com/entelecheia/gdelt-climaterisk/commit/9f0e53a1501c42f9339223f44b7d3da56a286eed))


## v0.2.0 (2024-11-02)

### Chores

* chore: update exclusion lists and add docker version variable in pyproject.toml ([`1f584f2`](https://github.com/entelecheia/gdelt-climaterisk/commit/1f584f2dad564ad46a06692816495437b61e19a1))

* chore(gkg_data): add datetime import to download_gdelt_gkg function ([`85e49d3`](https://github.com/entelecheia/gdelt-climaterisk/commit/85e49d317aeec33b79e00f247c95f43ef58c530f))

* chore: add pandas and gdelt dependencies to pyproject.toml ([`1d6e639`](https://github.com/entelecheia/gdelt-climaterisk/commit/1d6e6395c5aa12d53b3eabcfbea13d6c68931047))

* chore: add .Trash-* to .gitignore to exclude trash files ([`3b1fd10`](https://github.com/entelecheia/gdelt-climaterisk/commit/3b1fd10740cb6689c53e96538c4ffee85cb45d72))

* chore(docker): update Jupyter Lab notebook directory to use APP_SRC_DIR ([`fcadc80`](https://github.com/entelecheia/gdelt-climaterisk/commit/fcadc80fb12fb356652322fa85415eacc6334ad9))

* chore(docker): change default image variant to dev ([`db9317d`](https://github.com/entelecheia/gdelt-climaterisk/commit/db9317d276a581e954b8dd1fd5bceea6830ebe19))

### Features

* feat: add GDELT GKG data download and analysis functions ([`b9a05a5`](https://github.com/entelecheia/gdelt-climaterisk/commit/b9a05a5fe14f25894237283003e1a64dc0c2611b))

### Unknown

* Merge pull request #8 from entelecheia/main ([`a074d68`](https://github.com/entelecheia/gdelt-climaterisk/commit/a074d6875986de815f82323b91fefcdf3112ebc5))


## v0.1.0 (2024-11-02)

### Bug Fixes

* fix: update codecov token and copyright year in configuration ([`f1e0c6e`](https://github.com/entelecheia/gdelt-climaterisk/commit/f1e0c6e8c2c2aa3622f804240c0721ce93ffc808))

### Chores

* chore: comment out package publishing steps in release workflow for future reference ([`4d9b120`](https://github.com/entelecheia/gdelt-climaterisk/commit/4d9b120ff69d7282c5629c4f5d73420706242591))

* chore: remove obsolete Dockerfile.base to streamline container setup ([`22118fd`](https://github.com/entelecheia/gdelt-climaterisk/commit/22118fd368897ed93ad8f83c8806e947f2627c51))

* chore: improve project documentation and update README for clarity ([`332e4c6`](https://github.com/entelecheia/gdelt-climaterisk/commit/332e4c62b56f5ac7ce6033c9b117dd751fc8e76d))

* chore: add .envrc for project environment setup and virtual environment management ([`a6b4fd1`](https://github.com/entelecheia/gdelt-climaterisk/commit/a6b4fd19b4ed3675676d328cc68e2200e013f5f1))

* chore(release): update workflow for better release process ([`139eb37`](https://github.com/entelecheia/gdelt-climaterisk/commit/139eb3798117943a3411d6d8ca0ebb5bdd229348))

* chore(workflow): rename deploy-base-image to deploy-dev-image and update paths for development ([`813752f`](https://github.com/entelecheia/gdelt-climaterisk/commit/813752f8338d8952133e58dee62e3299f7978be1))

* chore(docker): update docker image variant name to 'dev' ([`30e8dc3`](https://github.com/entelecheia/gdelt-climaterisk/commit/30e8dc3ec37d3c48206470f8709265de3a479a8d))

* chore(docker): rename docker.base.env to docker.dev.env ([`14dbfc0`](https://github.com/entelecheia/gdelt-climaterisk/commit/14dbfc061063eca2a6fa56e30a04f3fe72817917))

* chore(docker): rename docker-compose.base.yaml to docker.dev.yaml ([`bc549a9`](https://github.com/entelecheia/gdelt-climaterisk/commit/bc549a9c9d577458c010d188c2da825f9b3c5535))

* chore: remove obsolete semantic release workflows ([`e5c7615`](https://github.com/entelecheia/gdelt-climaterisk/commit/e5c7615176f76cb2d2b2a69bcc72931bffbf79a8))

### Features

* feat: update pyproject.toml for semantic release configuration and dependency upgrades ([`30c3aee`](https://github.com/entelecheia/gdelt-climaterisk/commit/30c3aee57eca33178b75434a8c4b59b1c52ebc13))

* feat(docker): add development Dockerfile for GDELT Climate Risk project ([`38d4733`](https://github.com/entelecheia/gdelt-climaterisk/commit/38d4733d84736ecf09f810418363b42139d3bdf9))

* feat: add Docker configuration files and scripts for GDELT Climate Risk project ([`046bd71`](https://github.com/entelecheia/gdelt-climaterisk/commit/046bd71399e2ec0fe7af1e320d84062d4d4336f5))

* feat: add Docker commands to Makefile for local development ([`39f6eec`](https://github.com/entelecheia/gdelt-climaterisk/commit/39f6eec425e5a45772a3a9e9d49125af70bd8798))

* feat: add Copier Docker configuration for GDELT Climate Risk project ([`44cf083`](https://github.com/entelecheia/gdelt-climaterisk/commit/44cf0832c543cd2072fa7ba2d5427b0eb1873ea9))

* feat: add initial documentation, configuration files, and CLI implementation ([`9aca633`](https://github.com/entelecheia/gdelt-climaterisk/commit/9aca6334253efb5d417bf69a9ff63a4e1d4fd76b))

* feat: add initial project configuration files and Makefile ([`2f71068`](https://github.com/entelecheia/gdelt-climaterisk/commit/2f71068a73931facc723cb29e03ce33bd2e8d234))

### Unknown

* Merge pull request #7 from entelecheia/entelecheia/issue6 ([`0266abe`](https://github.com/entelecheia/gdelt-climaterisk/commit/0266abe4f626b885ae2020bccf3ab66574aaaac2))

* Merge pull request #4 from entelecheia/entelecheia/issue3 ([`ab664f0`](https://github.com/entelecheia/gdelt-climaterisk/commit/ab664f032ace9eb4d44dfd73641e86b6afafb229))

* Merge pull request #2 from entelecheia/entelecheia/issue1 ([`d535aa7`](https://github.com/entelecheia/gdelt-climaterisk/commit/d535aa7a802b26aac9a82b63810cccfb237918d9))

* Initial commit ([`113ff45`](https://github.com/entelecheia/gdelt-climaterisk/commit/113ff45d0e620369d10aafe7229e5710928cb769))
