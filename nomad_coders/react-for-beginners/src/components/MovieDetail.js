import PropTypes from "prop-types";
import { Link } from "react-router-dom";
function MovieDetail({ id, coverImg, title, summary, genres }) {
  return (
    <div>
      <img src={coverImg} alt={title} />
      <h1>
        <Link to={`/movie/${id}`}>{title}</Link>
      </h1>
      <h2>Summary</h2>
      <p>{summary}</p>
      <h3>Genres</h3>
      <ul>
        {genres.map((genres) => (
          <li key={genres}>{genres}</li>
        ))}
      </ul>
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

export default MovieDetail;
