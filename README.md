# What is this?

This repo contains server codes that include RouterManager, which performs routing for multiple django servers in a synchronous communication structure.


## Installation

1. Clone the repository
2. Install Redis in your computer and start Redis
3. Install PostgreSQL in your computer and start PostgreSQL
4. Install required packages
   ```
   pip3 install -r requirements.txt
   ```
5. Enter the PostgreSQL and Redis settings you installed into the .env file
6. Enter the Redis settings you installed into the router_manager_config.py file



## Usage

You can review the document I described for use.<br>
[Medium Document](https://tarkkabasakal.medium.com/redis-pub-sub-ile-birden-fazla-django-sunucusunda-eş-zamanlı-i̇letişim-kurulması-ab8abf30e7ec)



## License
[MIT](https://choosealicense.com/licenses/mit/)
