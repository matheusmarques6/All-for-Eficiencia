"""Checagem do parser do inventário. Asserts puros — sem framework."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import inventario
import slugs

FONTE = r"C:\Users\Usuario\Downloads\componentesinventario.md"


def main() -> None:
    vs = inventario.parse(FONTE)

    assert len(vs) == 44, f"esperava 44 variantes, veio {len(vs)}"

    por_secao = {}
    for v in vs:
        por_secao[v.secao] = por_secao.get(v.secao, 0) + 1
    assert por_secao == {
        "hero": 9, "body": 9, "products": 9,
        "reviews": 7, "offer": 6, "footer": 4,
    }, f"contagem por seção errada: {por_secao}"

    assert sum(1 for v in vs if not v.ativa) == 2, "esperava 2 variantes inativas"

    primeira = vs[0]
    assert primeira.ordem == "2.1"
    assert primeira.nome_no_banco == "hero section 10"
    assert primeira.variant_id == "dc6c363c-7d4f-4c70-a163-632bcadfdce6"
    assert primeira.secao == "hero"
    assert primeira.product_slots == 0
    assert primeira.densidade is None
    assert primeira.schema_campos == 4
    assert primeira.tags == []
    assert primeira.prosa["descricao_curta"].startswith('Diz "a solução é o conjunto')
    assert primeira.prosa["direcao_fotografica"].startswith("598 × 489px")

    # o typo do banco entra verbatim
    assert vs[1].nome_no_banco == "welcome - hero sectiion 8"
    assert vs[1].tags[0] == "dark_bg"

    # body 6: ativa, mas com os sete campos de prosa vazios
    b6 = next(v for v in vs if v.nome_no_banco == "body 6 - bridge skin minimalism 101")
    assert b6.ativa is True
    assert all(valor is None for valor in b6.prosa.values()), b6.prosa
    assert b6.schema_campos == 0

    # exatamente 4 variantes sem nenhum julgamento
    sem_julgamento = [v for v in vs if all(x is None for x in v.prosa.values())]
    assert len(sem_julgamento) == 4, [v.nome_no_banco for v in sem_julgamento]

    # exatamente 5 variantes com schema zerado
    assert sum(1 for v in vs if v.schema_campos == 0) == 5

    # a duplicata de review 3 tem ids distintos
    dups = [v for v in vs if v.nome_no_banco == "review 3"]
    assert len(dups) == 2 and dups[0].variant_id != dups[1].variant_id

    # a tabela de slugs cobre todas as variantes, sem colisão
    ids = {v.variant_id for v in vs}
    assert set(slugs.SLUG_POR_ID) == ids, "slugs.py não cobre exatamente os 44 ids"
    assert len(set(slugs.SLUG_POR_ID.values())) == 44, "slug duplicado"
    assert all(slugs.SECAO_POR_ID[v.variant_id] == v.secao for v in vs)

    print("ok: 44 variantes, prosa e slugs conferem")


if __name__ == "__main__":
    main()
