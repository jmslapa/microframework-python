from mf.http.middleware import Middleware

class TesteMiddleware(Middleware):
    
    def _before(self):
        # raise Exception('Middleware chamado antes')
        pass
    
    def _after(self, resource):
        # raise Exception(f'Middleware chamado depois. O recurso é: {resource}')
        pass
