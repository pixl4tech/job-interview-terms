import os
from fastapi import FastAPI
from job_terms_backend import endpoints


def create_app() -> FastAPI:

    # todo: meta information to config
    app = FastAPI(title="Job Term Dictionary App",
                    description="API for Job Term Dictionary App",
                    version="0.0.1",
                    terms_of_service="http://example.com/terms/",
                    contact={
                        "name": "Dmitry Kolosov",
                        "url": "https://kolosov.dev/contact/",
                        "email": "contact@kolosov.dev",
                    },
                    license_info={
                        "name": "Apache 2.0",
                        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                    })
    app.include_router(endpoints.term_router)
    return app


app = create_app()

