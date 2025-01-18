DROP TABLE IF EXISTS songs;

CREATE TABLE songs (
    id serial PRIMARY KEY,
    title varchar(255),
    artist_name varchar(255)
);

INSERT INTO songs (title, artist_name) VALUES
('Summer Without Internet', 'John Doe'),
('Starry Rain', 'Jane Smith'),
('City Under the Sole', 'Mike Johnson'),
('Blue Mood', 'Emily Davis'),
('You are Not Like That', 'Olivia Brown'),
('Heartbreaker', 'Sophia Miller'),
('Mazes', 'Liam Wilson'),
('Snow', 'Noah Taylor'),
('Slavic Sky', 'Isabella Anderson'),
('We Became Oceans', 'William Thomas'),
('They Are With Me', 'Emma Jackson'),
('Silver', 'Lucas White'),
('Winter in the Heart', 'Amelia Harris'),
('Sun of Monaco', 'Ethan Clark'),
('Nirvana', 'Ava Martin'),
('Black and White', 'Charlotte Lee'),
('Time-River', 'James Thompson'),
('Moscow Autumn', 'Oliver Martinez'),
('The Best Day', 'Mia Hernandez'),
('Dance', 'Benjamin Lopez');
