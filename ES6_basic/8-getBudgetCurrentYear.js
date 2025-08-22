function getCurrentYear() {
  return new Date().getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const y = getCurrentYear();
  return {
    [`income-${y}`]: income,
    [`gdp-${y}`]: gdp,
    [`capita-${y}`]: capita,
  };
} 