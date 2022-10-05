import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import MovieDetail from "../components/MovieDetail";

function Detail() {
  const [loading, setLoading] = useState(true);
  const [details, setDetails] = useState([]);
  const { id } = useParams();
  const getDetail = async () => {
    const yts = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json();
    setDetails(yts.data.movie);
    setLoading(false);
  };
  useEffect(() => {
    getDetail();
    //eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return (
    <div>
      {loading ? (
        <h1>Loading...</h1>
      ) : (
        <div>
          <MovieDetail
            coverImg={details.medium_cover_image}
            title={details.title}
            summary={details.description_full}
            genres={details.genres}
            key={details.id}
            id={details.id}
          />
        </div>
      )}
    </div>
  );
}

export default Detail;
