"""empty message

Revision ID: 3778071664a9
Revises: e0d9f3796588
Create Date: 2022-12-26 17:54:12.805822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3778071664a9"
down_revision = "e0d9f3796588"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cart",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "cart_items",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("cart_id", sa.Integer(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["cart_id"], ["cart.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_index("ix_category_id", table_name="category")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("ix_category_id", "category", ["id"], unique=False)
    op.drop_table("cart_items")
    op.drop_table("cart")
    # ### end Alembic commands ###
