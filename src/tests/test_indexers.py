from src.app.services.indexer import PointIndexer, PolygonIndexer
from src.app.services import entries


def test_point_indexer():
    indexer = PointIndexer()
    geopos = entries.PointGeopos(
        geometry={"type": "Point", "coordinates": [37.517259, 55.542444]},
        r=0
    )

    indexes = indexer.index(geopos)
    assert len(indexes) == 1

    geopos.r = 1
    indexes = indexer.index(geopos)
    assert len(indexes) == 7


def test_polygon_indexer():
    indexer = PolygonIndexer()
    geopos = entries.PolygonGeopos(
        geometry={
            "type": "Polygon",
            "coordinates": [[
                 [37.520123, 55.54413],
                 [37.515671, 55.54399],
                 [37.514662, 55.541793],
                 [37.521218, 55.542612],
                 [37.520123, 55.54413]
            ]]
        },
    )

    indexes = indexer.index(geopos)
    assert len(indexes) == 41

