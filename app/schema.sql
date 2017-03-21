DROP TABLE IF EXISTS fics;
CREATE TABLE fics (
    id integer primary key autoincrement,
    title text not null,
    url text not null,
    synopsis text not null,
    rating integer not null,
    comments text not null,
    length integer not null,
    author text not null,
    complete text not null,
    mood text not null,
    tvtropes text
);