import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Polygon, LayersControl } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const { BaseLayer, Overlay } = LayersControl;

export default function MapView() {
  const [tileUrls, setTileUrls] = useState(null);

  // Example AOI coordinates (same as backend)
  const aoiCoords = [
    [12.0, 77.0],
    [12.0, 77.8],
    [12.8, 77.8],
    [12.8, 77.0],
    [12.0, 77.0]
  ];

  useEffect(() => {
    fetch("http://localhost:8000/gee-tiles")
      .then(res => res.json())
      .then(data => setTileUrls(data));
  }, []);

  return (
    <div style={{ height: "600px", width: "100%" }}>
      <MapContainer center={[12.4, 77.4]} zoom={10} style={{ height: "100%", width: "100%" }}>
        <LayersControl position="topright">
          {tileUrls && (
            <>
              <BaseLayer checked name="Satellite">
                <TileLayer url={tileUrls.satellite} />
              </BaseLayer>
              <BaseLayer name="NDVI">
                <TileLayer url={tileUrls.ndvi} />
              </BaseLayer>
            </>
          )}
          <Overlay checked name="AOI Polygon">
            <Polygon positions={aoiCoords} pathOptions={{ color: "blue", weight: 2, fillOpacity: 0.1 }} />
          </Overlay>
        </LayersControl>
      </MapContainer>
    </div>
  );
}
