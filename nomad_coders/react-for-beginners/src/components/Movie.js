import PropTypes from "prop-types";
import { Link } from "react-router-dom";

function Movie({ id, coverImg, title, summary, genres }) {
  return (
    <div>
      <div className="flex mb-3 max-w-4xl mx-auto">
        <div className="w-[230px] h-[345px] shrink-0">
          <img src={coverImg} alt={title} />
        </div>
        <div className="flex flex-col justify-between ml-2 w-full">
          <div>
            <h1 className="mb-2">
              <Link to={`/movie/${id}`}>{title}</Link>
            </h1>
            <p>
              {summary.length > 730 ? `${summary.slice(0, 730)} ...` : summary}
            </p>
          </div>
          <ul className="flex">
            {genres.map((genres) => (
              <li key={genres}>{genres}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

Movie.propTypes = {
  coverImg: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
  id: PropTypes.number.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Movie;
