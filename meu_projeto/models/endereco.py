class Endereco:
    def __init__(self, local: str, numero: int) -> None:
        self.local = local
        self.numero = numero

    def __str__(self) -> str:
        return (
            f"\nLocal: {self.local}"  # Corrigido a capitalização de "local"
            f"\nNúmero: {self.numero}"
        )
