
CREATE TABLE Documents (
    doc_id INTEGER PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(1000) NOT NULL,
    author VARCHAR(100),
    creation_date DATE,
    content CLOB
);

CREATE TABLE Words (
    word_id INTEGER PRIMARY KEY,
    word VARCHAR(100) NOT NULL,
    CONSTRAINT unique_word UNIQUE (word)
);

CREATE TABLE WordLocations (
    location_id INTEGER PRIMARY KEY,
    word_id INTEGER,
    doc_id INTEGER,
    paragraph_num INTEGER,
    sentence_num INTEGER,
    word_position INTEGER,
    FOREIGN KEY (word_id) REFERENCES Words(word_id),
    FOREIGN KEY (doc_id) REFERENCES Documents(doc_id)
);

CREATE TABLE WordGroups (
    group_id INTEGER PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL,
    created_by VARCHAR(100),
    creation_date DATE
);

CREATE TABLE WordGroupMembers (
    group_id INTEGER,
    word_id INTEGER,
    PRIMARY KEY (group_id, word_id),
    FOREIGN KEY (group_id) REFERENCES WordGroups(group_id),
    FOREIGN KEY (word_id) REFERENCES Words(word_id)
);

CREATE TABLE Phrases (
    phrase_id INTEGER PRIMARY KEY,
    phrase_text VARCHAR(1000) NOT NULL,
    created_by VARCHAR(100),
    creation_date DATE
);

-- Search for documents containing a specific word
SELECT DISTINCT d.doc_id, d.file_name
FROM Documents d
JOIN WordLocations wl ON d.doc_id = wl.doc_id
JOIN Words w ON wl.word_id = w.word_id
WHERE w.word = 'example';

-- Find the most frequent words
SELECT w.word, COUNT(*) as frequency
FROM Words w
JOIN WordLocations wl ON w.word_id = wl.word_id
GROUP BY w.word
ORDER BY frequency DESC
LIMIT 10;

-- Find all words in a specific group
SELECT w.word
FROM Words w
JOIN WordGroupMembers wgm ON w.word_id = wgm.word_id
JOIN WordGroups wg ON wgm.group_id = wg.group_id
WHERE wg.group_name = 'Animals';

-- Find the context of a specific word (entire paragraph)
SELECT d.content
FROM Documents d
JOIN WordLocations wl ON d.doc_id = wl.doc_id
JOIN Words w ON wl.word_id = w.word_id
WHERE w.word = 'example'
AND SUBSTR(d.content,
    INSTR(d.content, '.', 1, wl.paragraph_num - 1) + 1,
    INSTR(d.content, '.', 1, wl.paragraph_num) -
    INSTR(d.content, '.', 1, wl.paragraph_num - 1)
) AS paragraph;

-- Count occurrences of each word in a specific document
SELECT w.word, COUNT(*) as word_count
FROM Words w
JOIN WordLocations wl ON w.word_id = wl.word_id
WHERE wl.doc_id = 1  -- Replace 1 with the desired document ID
GROUP BY w.word
ORDER BY word_count DESC;

-- Find documents containing a specific phrase
SELECT d.doc_id, d.file_name
FROM Documents d
JOIN PhraseLocations pl ON d.doc_id = pl.doc_id
JOIN Phrases p ON pl.phrase_id = p.phrase_id
WHERE p.phrase_text = 'example phrase';

-- Find the average number of words per sentence in each document
SELECT d.doc_id, d.file_name,
       COUNT(DISTINCT wl.word_id) / COUNT(DISTINCT wl.sentence_num) as avg_words_per_sentence
FROM Documents d
JOIN WordLocations wl ON d.doc_id = wl.doc_id
GROUP BY d.doc_id, d.file_name;

-- Find words that appear in all documents
SELECT w.word
FROM Words w
JOIN WordLocations wl ON w.word_id = wl.word_id
GROUP BY w.word_id, w.word
HAVING COUNT(DISTINCT wl.doc_id) = (SELECT COUNT(*) FROM Documents);


