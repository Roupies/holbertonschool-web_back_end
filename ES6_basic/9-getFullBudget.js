import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  return {
    ...budget,
    getIncomeInDollars(value) {
      return `$${value}`;
    },
    getIncomeInEuros(value) {
      return `${value} euros`;
    },
  };
} 