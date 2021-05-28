[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Build Status](https://cloud.drone.io/api/badges/gacerioni/tibia_monster_loot_item_id/status.svg)](https://cloud.drone.io/gacerioni/tibia_monster_loot_item_id)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/gabrielcerioni/harness_graphql_labs">
    <img src="images/harness_banner.jpeg" alt="Logo">
  </a>

  <h3 align="center">GraphQL Python Labs - by Gabs the CSE</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-and-usage">Installation and Usage</a></li>
      </ul>
    </li>
    <li><a href="#how-to-use-the-api">How to use the API</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The main goal of this project is to mantain a trustful source of Python GraphQL queries, to help Harness Customers.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [python3.6+](https://www.python.org/downloads/)

* For MacOs Users, please double-check the SSL CERT
   ```sh
   cd /Applications/Python\ 3.9/ # PUT YOUR PYTHON VERSION
   ./Install\ Certificates.command
   ```

### Installation and Usage

1. Clone the repo
   ```sh
   git clone https://github.com/gacerioni/tibia_monster_loot_item_id.git
   ```
2. Install the project dependecies (very simple stuff, meant to deal with requests, json, html)
   ```sh
   pip install -r requirements.txt
   ```
3. Enjoy ;)
   ```sh
   python main.py
   # Demon
   <...>
   ```
4. (Optional) If you want to run the API on your local env
   ```sh
   git clone https://github.com/gacerioni/tibia_monster_loot_item_id.git
   cd tibia_monster_loot_item_id
   pip install pipenv
   sudo pipenv shell
   pipenv install --dev
   export TIBIA_API_MONGODB_USR="<USER>"
   export TIBIA_API_MONGODB_PWD="<PWD>"
   cd ./api
   uvicorn main:app --reload
   ```

<!-- HOW TO USE THE API -->
## How to use the API

TODO

uvicorn main:app --reload

* [FastAPI Automatic Swagger Docs](http://127.0.0.1:8000/docs)
* [FastAPI Redoc Automatic Docs](http://127.0.0.1:8000/redoc)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/gacerioni/tibia_monster_loot_item_id/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Gabriel Cerioni - [@gabs.tar.gz](https://www.instagram.com/gabs.tar.gz/) - gacerioni@gmail.com

Project Link: [https://github.com/gacerioni/tibia_monster_loot_item_id/](https://github.com/gacerioni/tibia_monster_loot_item_id/)

<!-- Tech Stack -->
## Tech Stack

* [Python](https://www.python.org/)
* [MongoDB](https://www.mongodb.com/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)
* [FastAPI](https://fastapi.tiangolo.com/)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gabrielcerioni/harness_graphql_labs.svg?style=for-the-badge
[contributors-url]: https://github.com/gabrielcerioni/harness_graphql_labs/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gabrielcerioni/harness_graphql_labs.svg?style=for-the-badge
[forks-url]: https://github.com/gabrielcerioni/harness_graphql_labs/network/members
[stars-shield]: https://img.shields.io/github/stars/gabrielcerioni/harness_graphql_labs.svg?style=for-the-badge
[stars-url]: https://github.com/gabrielcerioni/harness_graphql_labs/stargazers
[issues-shield]: https://img.shields.io/github/issues/gabrielcerioni/harness_graphql_labs.svg?style=for-the-badge
[issues-url]: https://github.com/gabrielcerioni/harness_graphql_labs/issues
[license-shield]: https://img.shields.io/github/license/gabrielcerioni/harness_graphql_labs.svg?style=for-the-badge
[license-url]: https://github.com/gabrielcerioni/harness_graphql_labs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gabrielcerioni
[product-screenshot]: images/gabs_tibia.png
[api_postman_all]: images/Postman_API_ALL.png
[api_postman_id]: images/Postman_API_by_id.png
[api_postman_name]: images/Postman_API_by_name.png
