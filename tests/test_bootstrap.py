from jarvis.bootstrap import (
    JarvisBootstrap,
)



def test_bootstrap():

    bootstrap = JarvisBootstrap()


    container = bootstrap.start()


    assert container is not None