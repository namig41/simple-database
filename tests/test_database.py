def test_set_and_get(db):
    """Тестирование операций set и get."""
    db.set("A", 10)
    assert db.get("A") == 10

    db.set("B", 20)
    assert db.get("B") == 20

    assert db.get("C") is None


def test_unset(db):
    """Тестирование операции unset."""
    db.set("A", 10)
    db.unset("A")
    assert db.get("A") is None

    db.unset("B")
    assert db.get("B") is None


def test_counts(db):
    """Тестирование операции counts."""
    db.set("A", 10)
    db.set("B", 10)
    db.set("C", 20)

    assert db.counts(10) == 2
    assert db.counts(20) == 1
    assert db.counts(30) == 0


def test_find(db):
    """Тестирование операции find."""
    db.set("A", 10)
    db.set("B", 10)
    db.set("C", 20)

    assert sorted(db.find(10)) == ["A", "B"]
    assert sorted(db.find(20)) == ["C"]
    assert db.find(30) == []


def test_begin(db):
    """Тестирование начала транзакции и операций в транзакции."""
    db.set("A", 10)
    db.begin()

    db.set("B", 20)
    assert db.get("B") == 20

    db.rollback()
    assert db.get("B") is None
    assert db.get("A") == 10


def test_commit_transaction(db):
    """Тестирование операции commit."""
    db.set("A", 10)
    db.begin()

    db.set("B", 20)
    assert db.get("B") == 20

    db.commit()
    assert db.get("A") == 10
    assert db.get("B") == 20


def test_rollback_transaction(db):
    """Тестирование отката транзакции."""
    db.set("A", 10)
    db.begin()

    db.set("B", 20)
    assert db.get("B") == 20

    db.rollback()
    assert db.get("B") is None
    assert db.get("A") == 10


def test_nested_transactions(db):
    """Тестирование вложенных транзакций."""
    db.set("A", 10)
    db.begin()

    db.set("B", 20)
    db.begin()

    db.set("C", 30)
    assert db.get("C") == 30

    db.rollback()
    assert db.get("C") is None

    db.commit()
