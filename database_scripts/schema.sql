-- Create tables for Django models
CREATE TABLE concordance_document
(
    id          NUMBER(11) PRIMARY KEY,
    title       VARCHAR2(255) NOT NULL,
    content     CLOB      NOT NULL,
    upload_date TIMESTAMP NOT NULL
);

CREATE TABLE concordance_metadata
(
    id          NUMBER(11) PRIMARY KEY,
    document_id NUMBER(11) NOT NULL,
    key         VARCHAR2(100) NOT NULL,
    value       VARCHAR2(255) NOT NULL,
    FOREIGN KEY (document_id) REFERENCES concordance_document (id)
);

CREATE TABLE concordance_word
(
    id   NUMBER(11) PRIMARY KEY,
    text VARCHAR2(100) UNIQUE NOT NULL
);

CREATE TABLE concordance_wordoccurrence
(
    id          NUMBER(11) PRIMARY KEY,
    word_id     NUMBER(11) NOT NULL,
    document_id NUMBER(11) NOT NULL,
    position    NUMBER(11) NOT NULL,
    FOREIGN KEY (word_id) REFERENCES concordance_word (id),
    FOREIGN KEY (document_id) REFERENCES concordance_document (id)
);

CREATE TABLE concordance_wordgroup
(
    id   NUMBER(11) PRIMARY KEY,
    name VARCHAR2(100) NOT NULL
);

CREATE TABLE concordance_wordgroup_words
(
    id           NUMBER(11) PRIMARY KEY,
    wordgroup_id NUMBER(11) NOT NULL,
    word_id      NUMBER(11) NOT NULL,
    FOREIGN KEY (wordgroup_id) REFERENCES concordance_wordgroup (id),
    FOREIGN KEY (word_id) REFERENCES concordance_word (id)
);

CREATE TABLE concordance_linguisticexpression
(
    id          NUMBER(11) PRIMARY KEY,
    expression  VARCHAR2(255) NOT NULL,
    description CLOB NOT NULL
);

-- Create sequences for auto-incrementing IDs
CREATE SEQUENCE concordance_document_seq;
CREATE SEQUENCE concordance_metadata_seq;
CREATE SEQUENCE concordance_word_seq;
CREATE SEQUENCE concordance_wordoccurrence_seq;
CREATE SEQUENCE concordance_wordgroup_seq;
CREATE SEQUENCE concordance_wordgroup_words_seq;
CREATE SEQUENCE concordance_linguisticexpression_seq;

-- Create triggers for auto-incrementing IDs
CREATE
OR REPLACE TRIGGER concordance_document_tr
BEFORE INSERT ON concordance_document
FOR EACH ROW
BEGIN
SELECT concordance_document_seq.NEXTVAL
INTO :new.id
FROM dual;
END;
/

-- Create similar triggers for other tables